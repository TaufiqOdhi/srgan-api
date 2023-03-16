import torch
import os
import ai.config as config
import numpy as np
import pydicom
from torchvision.utils import make_grid
from PIL import Image
from torchvision.utils import save_image
from albumentations import Resize

def gradient_penalty(critic, real, fake, device):
    BATCH_SIZE, C, H, W = real.shape
    alpha = torch.rand((BATCH_SIZE, 1, 1, 1)).repeat(1, C, H, W).to(device)
    interpolated_images = real * alpha + fake.detach() * (1 - alpha)
    interpolated_images.requires_grad_(True)

    # Calculate critic scores
    mixed_scores = critic(interpolated_images)

    # Take the gradient of the scores with respect to the images
    gradient = torch.autograd.grad(
        inputs=interpolated_images,
        outputs=mixed_scores,
        grad_outputs=torch.ones_like(mixed_scores),
        create_graph=True,
        retain_graph=True,
    )[0]
    gradient = gradient.view(gradient.shape[0], -1)
    gradient_norm = gradient.norm(2, dim=1)
    gradient_penalty = torch.mean((gradient_norm - 1) ** 2)
    return gradient_penalty


def save_checkpoint(model, optimizer, filename="my_checkpoint.pth.tar"):
    print("=> Saving checkpoint")
    checkpoint = {
        "state_dict": model.state_dict(),
        "optimizer": optimizer.state_dict(),
    }
    torch.save(checkpoint, filename)


def load_checkpoint(checkpoint_file, model, optimizer, lr):
    print("=> Loading checkpoint")
    checkpoint = torch.load(checkpoint_file, map_location=config.DEVICE)
    model.load_state_dict(checkpoint["state_dict"])
    optimizer.load_state_dict(checkpoint["optimizer"])

    # If we don't do this then it will just have learning rate of old checkpoint
    # and it will lead to many hours of debugging \:
    for param_group in optimizer.param_groups:
        param_group["lr"] = lr


def plot_examples(low_res_folder, gen):
    if os.name == 'posix':
        os.system("rm saved/*")
    elif os.name == 'nt':
        os.system("powershell rm saved/*") # for running in windows system
    files = os.listdir(low_res_folder)
    np.random.shuffle(files)
    gen.eval()
    for file in files[:5]:
        image = Image.open(low_res_folder + file)
        # image = pydicom.read_file(low_res_folder+file).pixel_array
        try:
            with torch.no_grad():
                upscaled_img = gen(
                    config.test_transform(image=np.asarray(image))["image"]
                    .unsqueeze(0)
                    .to(config.DEVICE)
                )
            save_image(upscaled_img * 0.5 + 0.5, f"saved/{file}")
        except FileNotFoundError:
            pass
        except:
            print('Memory insufficient for that image')
    gen.train()

def compress(img: np.ndarray, ratio:int):
    resized = Resize(width=img.shape[1]//ratio, height=img.shape[0]//ratio, interpolation=Image.BICUBIC)(image=img)["image"]
    return resized

def bit8to4(img):
    return (img//16).astype(np.uint8)

def bit4to8(img):
    return img*16

def split(img):
    bottom_img = bit8to4(img)
    top_img = img - bottom_img*16
    return np.vstack((top_img, bottom_img))

def recovery_binary(img):
    split_img = split(img)
    img_8_bit = bit4to8(split_img)

    return img_8_bit

def recovery_srgan(img, gen):
    with torch.no_grad():
        upscaled_img = gen(
            config.test_transform(image=np.asarray(img))["image"]
            .unsqueeze(0)
            .to(config.DEVICE)
        )
        upscaled_img = upscaled_img * 0.5 + 0.5
        upscaled_img = make_grid(upscaled_img)
        upscaled_img = upscaled_img.mul(255).add_(0.5).clamp_(0, 255).permute(1, 2, 0).to("cpu", torch.uint8).numpy()
        
        return upscaled_img
