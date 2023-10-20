import datetime
import json
import gspread
from io import BytesIO
from fastapi import File, Form, UploadFile
import subprocess
import os
from pathlib import Path
from minio.error import S3Error
from minio_connection import minio_client, bucket_name
from redis_connection import redis_client
from google.oauth2.credentials import Credentials
from login_gsheet import SCOPES, TOKEN_LOCATION


async def no_prune(image: UploadFile = File(), filename: str = Form()):
    start_timestamp = datetime.datetime.now()
    input_filename = f'{filename}_no_prune_{datetime.datetime.now()}{Path(image.filename).suffix}'
    minio_host = os.popen("docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' minio-server").read()
    # ip_host = os.popen("ip addr | awk '/inet/ && /wlo1/ {print $2}'").read().split('/')[0]
    # minio_host = ip_host
    ip_host = os.popen("ip addr | awk '/inet/ && /docker0/ {print $2}'").read().split('/')[0]

    # Upload FIle to Minio bucket
    minio_client.put_object(
        bucket_name=f'{bucket_name}',
        object_name=f'input_files/{input_filename}',
        data=image.file,
        length=-1,  # Unknown size, read till EOF,
        part_size=5 << 20 # 5MB chunks
    )

    # enqueue to redis
    redis_client.lpush('srgan', json.dumps(dict(
        filename=input_filename,
        image_name='srgan-ai-module:no_prune',
        ai_type='srgan'
    )))


    # nanti disebelah sini akan dijalankan sebuah metode untuk menentukan proses yang datang ini akan
    # dimasukkan pada worker mana ?
    # 

    # dequeue from redis
    item = json.loads(redis_client.rpop('srgan').decode('utf-8'))
    print(item)

    cmd = ["docker", "run", "--rm", "--runtime", 'nvidia',
           "-v", os.path.expanduser("~/Projects/Thesis/input_files:/app/input_files"),
           "-v", os.path.expanduser("~/Projects/Thesis/output_files:/app/output_files"),
           "-e", f'FILENAME={input_filename}', "-e", f"MINIO_HOST={minio_host}",
           "-e", f'IP_HOST={ip_host}', "-e", f"START_TIMESTAMP={start_timestamp}",
           "taufiqodhi/srgan-ai-module:no_prune"]
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

async def vram_logs(filename: str = Form(), start_timestamp: str = Form(), image_filename: str = Form()):
    vram_log = os.popen('nvidia-smi').read()

    gsheet_client = gspread.Client(Credentials.from_authorized_user_file(TOKEN_LOCATION, SCOPES))
    spreadsheet = gsheet_client.open_by_url('https://docs.google.com/spreadsheets/d/1PaFime-HZc-U9Zt3MwzZLolC5BMQWTauUuqZ_JRNIhI/edit#gid=0')
    sheet = spreadsheet.get_worksheet(0)
    sheet.append_row([f'http://localhost:9000/super-resolution/input_files/{image_filename}',
                      f'http://localhost:9000/super-resolution/output_files/{image_filename}',
                      f'http://localhost:9000/super-resolution/vram_logs/{filename}',
                      start_timestamp, datetime.datetime.now().__str__()])
    
    minio_client.put_object(
        bucket_name=bucket_name,
        object_name=f'vram_logs/{filename}',
        data=BytesIO(bytes(vram_log, 'utf-8')),
        length=len(vram_log)
    )
    return vram_log