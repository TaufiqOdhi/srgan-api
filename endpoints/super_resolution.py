import datetime
from io import BytesIO
from fastapi import File, Form, UploadFile
import subprocess
import os
from pathlib import Path
from minio.error import S3Error
from minio_connection import minio_client, bucket_name


async def no_prune(image: UploadFile = File(), filename: str = Form()):
    input_filename = f'{filename}_no_prune_{datetime.datetime.now()}{Path(image.filename).suffix}'
    minio_host = os.popen("docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' minio-server").read()
    ip_host = os.popen("ip addr | awk '/inet/ && /docker0/ {print $2}'").read().split('/')[0]

    # Upload FIle to Minio bucket
    minio_client.put_object(
        bucket_name=f'{bucket_name}',
        object_name=f'input_files/{input_filename}',
        data=image.file,
        length=-1,  # Unknown size, read till EOF,
        part_size=5 << 20 # 5MB chunks
    )
    cmd = ["docker", "run", "--rm", "--runtime", 'nvidia',
           "-v", os.path.expanduser("~/Projects/Thesis/input_files:/app/input_files"),
           "-v", os.path.expanduser("~/Projects/Thesis/output_files:/app/output_files"),
           "-e", f'FILENAME={input_filename}', "-e", f"MINIO_HOST={minio_host}",
           "-e", f'IP_HOST={ip_host}',"taufiqodhi/srgan-ai-module:no_prune"]
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

async def l1_norm_30(image: UploadFile = File(), filename: str = Form()):
    input_filename = f'{filename}_l1_norm_30_{datetime.datetime.now()}{Path(image.filename).suffix}'
    input_file = os.path.expanduser(f'~/Projects/Thesis/input_files/{input_filename}')
    with open(input_file, "wb+") as file_object:
        file_object.write(image.file.read())
        file_object.close()
    cmd = ["docker", "run", "--rm", "--runtime", 'nvidia',
           "-v", os.path.expanduser("~/Projects/Thesis/input_files:/app/input_files"),
           "-v", os.path.expanduser("~/Projects/Thesis/output_files:/app/output_files"),
           "-e", f'FILENAME={input_filename}', "taufiqodhi/srgan-ai-module:l1_norm-30"]
    completed_process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    return dict(result=completed_process.stdout, error=completed_process.stderr)

async def l1_norm_50(image: UploadFile = File(), filename: str = Form()):
    input_filename = f'{filename}_l1_norm_50_{datetime.datetime.now()}{Path(image.filename).suffix}'
    input_file = os.path.expanduser(f'~/Projects/Thesis/input_files/{input_filename}')
    with open(input_file, "wb+") as file_object:
        file_object.write(image.file.read())
        file_object.close()
    cmd = ["docker", "run", "--rm", "--runtime", 'nvidia',
           "-v", os.path.expanduser("~/Projects/Thesis/input_files:/app/input_files"),
           "-v", os.path.expanduser("~/Projects/Thesis/output_files:/app/output_files"),
           "-e", f'FILENAME={input_filename}', "taufiqodhi/srgan-ai-module:l1_norm-50"]
    completed_process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    return dict(result=completed_process.stdout, error=completed_process.stderr)

async def l1_norm_70(image: UploadFile = File(), filename: str = Form()):
    input_filename = f'{filename}_l1_norm_70_{datetime.datetime.now()}{Path(image.filename).suffix}'
    input_file = os.path.expanduser(f'~/Projects/Thesis/input_files/{input_filename}')
    with open(input_file, "wb+") as file_object:
        file_object.write(image.file.read())
        file_object.close()
    cmd = ["docker", "run", "--rm", "--runtime", 'nvidia',
           "-v", os.path.expanduser("~/Projects/Thesis/input_files:/app/input_files"),
           "-v", os.path.expanduser("~/Projects/Thesis/output_files:/app/output_files"),
           "-e", f'FILENAME={input_filename}', "taufiqodhi/srgan-ai-module:l1_norm-70"]
    completed_process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    return dict(result=completed_process.stdout, error=completed_process.stderr)

async def l2_norm_30(image: UploadFile = File(), filename: str = Form()):
    input_filename = f'{filename}_l2_norm_30_{datetime.datetime.now()}{Path(image.filename).suffix}'
    input_file = os.path.expanduser(f'~/Projects/Thesis/input_files/{input_filename}')
    with open(input_file, "wb+") as file_object:
        file_object.write(image.file.read())
        file_object.close()
    cmd = ["docker", "run", "--rm", "--runtime", 'nvidia',
           "-v", os.path.expanduser("~/Projects/Thesis/input_files:/app/input_files"),
           "-v", os.path.expanduser("~/Projects/Thesis/output_files:/app/output_files"),
           "-e", f'FILENAME={input_filename}', "taufiqodhi/srgan-ai-module:l2_norm-30"]
    completed_process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    return dict(result=completed_process.stdout, error=completed_process.stderr)

async def l2_norm_50(image: UploadFile = File(), filename: str = Form()):
    input_filename = f'{filename}_l2_norm_50_{datetime.datetime.now()}{Path(image.filename).suffix}'
    input_file = os.path.expanduser(f'~/Projects/Thesis/input_files/{input_filename}')
    with open(input_file, "wb+") as file_object:
        file_object.write(image.file.read())
        file_object.close()
    cmd = ["docker", "run", "--rm", "--runtime", 'nvidia',
           "-v", os.path.expanduser("~/Projects/Thesis/input_files:/app/input_files"),
           "-v", os.path.expanduser("~/Projects/Thesis/output_files:/app/output_files"),
           "-e", f'FILENAME={input_filename}', "taufiqodhi/srgan-ai-module:l2_norm-50"]
    completed_process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    return dict(result=completed_process.stdout, error=completed_process.stderr)

async def l2_norm_70(image: UploadFile = File(), filename: str = Form()):
    input_filename = f'{filename}_l2_norm_70_{datetime.datetime.now()}{Path(image.filename).suffix}'
    input_file = os.path.expanduser(f'~/Projects/Thesis/input_files/{input_filename}')
    with open(input_file, "wb+") as file_object:
        file_object.write(image.file.read())
        file_object.close()
    cmd = ["docker", "run", "--rm", "--runtime", 'nvidia',
           "-v", os.path.expanduser("~/Projects/Thesis/input_files:/app/input_files"),
           "-v", os.path.expanduser("~/Projects/Thesis/output_files:/app/output_files"),
           "-e", f'FILENAME={input_filename}', "taufiqodhi/srgan-ai-module:l2_norm-70"]
    completed_process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    return dict(result=completed_process.stdout, error=completed_process.stderr)

async def vram_logs(filename: str = Form()):
    vram_log = bytes(os.popen('nvidia-smi').read(), 'utf-8')
    minio_client.put_object(
        bucket_name=bucket_name,
        object_name=f'vram_logs/{filename}',
        data=BytesIO(vram_log),
        length=len(vram_log)
    )
    return vram_log.decode()