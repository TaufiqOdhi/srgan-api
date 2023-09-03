import numpy as np
import torch
import datetime
from fastapi import File, Form, UploadFile
from PIL import Image
from ai.compress import compress_binary, recovery_srgan, recovery_binary
from ai.model.prune_l1_norm import GeneratorPruned as GeneratorL1Norm
from ai.model.prune_l2_norm import GeneratorPruned as GeneratorL2Norm
from ai.config import DEVICE
import subprocess
import os
from pathlib import Path


base_dir_checkpoint = 'ai/checkpoints'


def _srgan(gen, image, CKPT_PTH, filename, srgan_type):
    file_path = f'saved_files/{filename}_{srgan_type}_{datetime.datetime.now()}.png'
    gen.load_state_dict(torch.load(CKPT_PTH)["state_dict"])
    gen.eval().to(DEVICE)

    input_image = np.asarray(Image.open(image.file))
    input_image = compress_binary(input_image)
    input_image = recovery_binary(input_image)
    input_image = recovery_srgan(img=input_image, gen=gen)
    Image.fromarray(input_image).save(file_path)

    return file_path
    

async def no_prune(image: UploadFile = File(), filename: str = Form()):
    input_filename = f'{filename}_no_prune_{datetime.datetime.now()}{Path(image.filename).suffix}'
    input_file = os.path.expanduser(f'~/Projects/Thesis/input_files/{input_filename}')
    with open(input_file, "wb+") as file_object:
        file_object.write(image.file.read())
        file_object.close()
    cmd = ["docker", "run", "--rm", "--runtime", 'nvidia',
           "-v", os.path.expanduser("~/Projects/Thesis/input_files:/app/input_files"),
           "-v", os.path.expanduser("~/Projects/Thesis/output_files:/app/output_files"),
           "-e", f'FILENAME={input_filename}', "taufiqodhi/srgan-ai-module:no_prune"]
    completed_process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    return dict(result=completed_process.stdout, error=completed_process.stderr)
    

async def random_unstructured_30(image: UploadFile = File(), filename: str = Form()):
    input_filename = f'{filename}_random_unstructured_30_{datetime.datetime.now()}{Path(image.filename).suffix}'
    input_file = os.path.expanduser(f'~/Projects/Thesis/input_files/{input_filename}')
    with open(input_file, "wb+") as file_object:
        file_object.write(image.file.read())
        file_object.close()
    cmd = ["docker", "run", "--rm", "--runtime", 'nvidia',
           "-v", os.path.expanduser("~/Projects/Thesis/input_files:/app/input_files"),
           "-v", os.path.expanduser("~/Projects/Thesis/output_files:/app/output_files"),
           "-e", f'FILENAME={input_filename}', "taufiqodhi/srgan-ai-module:random_unstructured-30"]
    completed_process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    return dict(result=completed_process.stdout, error=completed_process.stderr)


async def random_unstructured_50(image: UploadFile = File(), filename: str = Form()):
    input_filename = f'{filename}_random_unstructured_50_{datetime.datetime.now()}{Path(image.filename).suffix}'
    input_file = os.path.expanduser(f'~/Projects/Thesis/input_files/{input_filename}')
    with open(input_file, "wb+") as file_object:
        file_object.write(image.file.read())
        file_object.close()
    cmd = ["docker", "run", "--rm", "--runtime", 'nvidia',
           "-v", os.path.expanduser("~/Projects/Thesis/input_files:/app/input_files"),
           "-v", os.path.expanduser("~/Projects/Thesis/output_files:/app/output_files"),
           "-e", f'FILENAME={input_filename}', "taufiqodhi/srgan-ai-module:random_unstructured-50"]
    completed_process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    return dict(result=completed_process.stdout, error=completed_process.stderr)

async def random_unstructured_70(image: UploadFile = File(), filename: str = Form()):
    input_filename = f'{filename}_random_unstructured_70_{datetime.datetime.now()}{Path(image.filename).suffix}'
    input_file = os.path.expanduser(f'~/Projects/Thesis/input_files/{input_filename}')
    with open(input_file, "wb+") as file_object:
        file_object.write(image.file.read())
        file_object.close()
    cmd = ["docker", "run", "--rm", "--runtime", 'nvidia',
           "-v", os.path.expanduser("~/Projects/Thesis/input_files:/app/input_files"),
           "-v", os.path.expanduser("~/Projects/Thesis/output_files:/app/output_files"),
           "-e", f'FILENAME={input_filename}', "taufiqodhi/srgan-ai-module:random_unstructured-70"]
    completed_process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    return dict(result=completed_process.stdout, error=completed_process.stderr)

async def l1_norm(image: UploadFile = File(), filename: str = Form(), prune_amount: int = Form()):
    CKPT_PTH = f'{base_dir_checkpoint}/l1normGlobal_pruned_176_epoch/{prune_amount}/3_dim/gen.pth.tar'
    gen = GeneratorL1Norm()
    return _srgan(
        gen=gen,
        image=image,
        CKPT_PTH=CKPT_PTH,
        filename=filename,
        srgan_type=f'{prune_amount}l1Norm'
    )

async def l2_norm(image: UploadFile = File(), filename: str = Form(), prune_amount: int = Form()):
    CKPT_PTH = f'{base_dir_checkpoint}/l2normGlobal_pruned_176_epoch/{prune_amount}/3_dim/gen.pth.tar'
    gen = GeneratorL2Norm()
    return _srgan(
        gen=gen,
        image=image,
        CKPT_PTH=CKPT_PTH,
        filename=filename,
        srgan_type=f'{prune_amount}l2Norm'
    )
