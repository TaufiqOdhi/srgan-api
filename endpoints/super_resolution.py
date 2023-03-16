import numpy as np
import torch
import datetime
from fastapi import File, Form, UploadFile
from PIL import Image
from ai.compress import compress_binary, recovery_srgan, recovery_binary
from ai.model import Generator
from ai.model.prune_random_unstructured_global import GeneratorPruned as GeneratorRandomUnstructured
from ai.model.prune_l1_norm import GeneratorPruned as GeneratorL1Norm
from ai.model.prune_l2_norm import GeneratorPruned as GeneratorL2Norm
from ai.config import DEVICE


base_dir_checkpoint = '/mnt/Windows/Users/taufi/MyFile/Projects/image-compression-restoration/04_1_binaryCompression_srganRecovery_layerWisePruning/checkpoints'


def _srgan(gen, image, CKPT_PTH, filename):
    file_path = f'saved_files/{filename}_{datetime.datetime.now()}.png'
    gen.load_state_dict(torch.load(CKPT_PTH)["state_dict"])
    gen.eval().to(DEVICE)

    input_image = np.asarray(Image.open(image.file))
    input_image = compress_binary(input_image)
    input_image = recovery_binary(input_image)
    input_image = recovery_srgan(img=input_image, gen=gen)
    Image.fromarray(input_image).save(file_path)

    return file_path
    

async def no_prune(image: UploadFile = File(), filename: str = Form()):
    CKPT_PTH = f'{base_dir_checkpoint}/no_prune/gen.pth.tar'
    gen = Generator()
    return _srgan(
        gen=gen,
        image=image,
        CKPT_PTH=CKPT_PTH,
        filename=filename
    )

async def random_unstructured(image: UploadFile = File(), filename: str = Form(), prune_amount: int = Form()):
    CKPT_PTH = f'{base_dir_checkpoint}/randomUnstructuredGlobal/176-epoch-pruned-model/{prune_amount}/gen.pth.tar'
    gen = GeneratorRandomUnstructured()
    return _srgan(
        gen=gen,
        image=image,
        CKPT_PTH=CKPT_PTH,
        filename=filename
    )

async def l1_norm(image: UploadFile = File(), filename: str = Form(), prune_amount: int = Form()):
    CKPT_PTH = f'{base_dir_checkpoint}/l1normGlobal_pruned_176_epoch/{prune_amount}/gen.pth.tar'
    gen = GeneratorRandomUnstructured()
    return _srgan(
        gen=gen,
        image=image,
        CKPT_PTH=CKPT_PTH,
        filename=filename
    )

async def l2_norm(image: UploadFile = File(), filename: str = Form(), prune_amount: int = Form()):
    CKPT_PTH = f'{base_dir_checkpoint}/l2normGlobal_pruned_176_epoch/{prune_amount}/gen.pth.tar'
    gen = GeneratorRandomUnstructured()
    return _srgan(
        gen=gen,
        image=image,
        CKPT_PTH=CKPT_PTH,
        filename=filename
    )
