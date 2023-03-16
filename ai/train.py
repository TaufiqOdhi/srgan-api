import torch
import ai.config as config
from torch import nn
from torch import optim
from ai.utils import load_checkpoint, save_checkpoint, plot_examples
from ai.loss import VGGLoss
from torch.utils.data import DataLoader
from ai.model import Discriminator
from tqdm import tqdm
from ai.dataset import MyImageFolder

torch.backends.cudnn.benchmark = True


def train_fn(loader, disc, gen, opt_gen, opt_disc, mse, bce, vgg_loss):
    loop = tqdm(loader, leave=True)

    for idx, (low_res, high_res) in enumerate(loop):
        high_res = high_res.to(config.DEVICE)
        low_res = low_res.to(config.DEVICE)
        
        ### Train Discriminator: max log(D(x)) + log(1 - D(G(z)))
        fake = gen(low_res)
        disc_real = disc(high_res)
        disc_fake = disc(fake.detach())
        disc_loss_real = bce(
            disc_real, torch.ones_like(disc_real) - 0.1 * torch.rand_like(disc_real)
        )
        disc_loss_fake = bce(disc_fake, torch.zeros_like(disc_fake))
        
        loss_disc = disc_loss_fake + disc_loss_real
        # print(f'discrimantor loss:{loss_disc}')

        opt_disc.zero_grad()
        loss_disc.backward()
        opt_disc.step()

        # Train Generator: min log(1 - D(G(z))) <-> max log(D(G(z))
        disc_fake = disc(fake)
        l2_loss = mse(fake, high_res)
        adversarial_loss = bce(disc_fake, torch.ones_like(disc_fake))
        
        loss_for_vgg = vgg_loss(fake, high_res)
        # gen_loss = loss_for_vgg + adversarial_loss + l2_loss
        gen_loss = 6e-2 * loss_for_vgg + 1e-2 * adversarial_loss + 0.92*l2_loss
        # print(f'Generative loss:{gen_loss}')

        opt_gen.zero_grad()
        gen_loss.backward()
        opt_gen.step()

        if idx % 200 == 0:
            plot_examples(config.VAL_PATH, gen)
            print(f'discrimantor loss:{loss_disc}')
            print(f'Generative loss:{gen_loss}')

    return (loss_disc, gen_loss)


def main(pruned_model='random unstructured global'):
    print(pruned_model)
    if pruned_model == 'l1 norm':
        from model.prune_l1_norm import GeneratorPruned
    elif pruned_model == 'l2 norm':
        from model.prune_l2_norm import GeneratorPruned
    elif pruned_model == 'random unstructured global':
        from model.prune_random_unstructured_global import GeneratorPruned
    else:
        return


    dataset = MyImageFolder(root_dir=config.TRAIN_PATH)
    loader = DataLoader(
        dataset,
        batch_size=config.BATCH_SIZE,
        shuffle=True,
        pin_memory=True,
        num_workers=config.NUM_WORKERS,
    )


    gen = GeneratorPruned(in_channels=3, ratio=config.RATIO).to(config.DEVICE)
    disc = Discriminator(in_channels=3).to(config.DEVICE)
    opt_gen = optim.Adam(gen.parameters(), lr=config.LEARNING_RATE, betas=(0.9, 0.999))
    opt_disc = optim.Adam(disc.parameters(), lr=config.LEARNING_RATE, betas=(0.9, 0.999))
    mse = nn.MSELoss()
    bce = nn.BCEWithLogitsLoss()
    vgg_loss = VGGLoss()

    
    if config.LOAD_MODEL:
        try:
            load_checkpoint(
                config.CHECKPOINT_GEN,
                gen,
                opt_gen,
                config.LEARNING_RATE,
            )
            load_checkpoint(
                config.CHECKPOINT_DISC, disc, opt_disc, config.LEARNING_RATE,
            )
        except FileNotFoundError:
            pass

    for epoch in range(config.START_EPOCHS-1,config.NUM_EPOCHS):
        print(f'======================EPOCH: {epoch+1}=====================')
        loss_disc, gen_loss = train_fn(loader, disc, gen, opt_gen, opt_disc, mse, bce, vgg_loss)

        if config.SAVE_MODEL:
            save_checkpoint(gen, opt_gen, filename=config.CHECKPOINT_GEN)
            save_checkpoint(disc, opt_disc, filename=config.CHECKPOINT_DISC)
            f = open("current_complete_epoch.txt", "w")
            f.write(f"{pruned_model}\n{epoch+1}")
            f.write(f'\ndiscrimantor loss:{loss_disc}')
            f.write(f'\nGenerative loss:{gen_loss}')
            f.write(f'\nPrune Amount: {config.PRUNE_AMOUNT}')
            f.close()
        
        print(pruned_model)


if __name__ == "__main__":
    main()