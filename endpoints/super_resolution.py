import datetime
import json
import gspread
import requests
from io import BytesIO
from fastapi import File, Form, UploadFile
import subprocess
import os
from pathlib import Path
from minio_connection import minio_client, bucket_name
from redis_connection import redis_client
from google.oauth2.credentials import Credentials
from login_gsheet import SCOPES, TOKEN_LOCATION
from rq import Queue


NODE_WORKER = 'Odhi-Laptop'


async def no_prune(image: UploadFile = File(), filename: str = Form(), node_worker  : str = Form(), queue_name : str = Form(), start_timestamp : str = Form()):
    input_filename = f'{filename}_no_prune_{start_timestamp}{Path(image.filename).suffix}'
    
    # ip_host = node_worker
    # minio_host = os.popen("ip addr | awk '/inet/ && /eno1/ {print $2}'").read().split('/')[0]
    # minio_host = os.popen("ip addr | awk '/inet/ && /wlo1/ {print $2}'").read().split('/')[0]
    # ip_host = os.popen("ip addr | awk '/inet/ && /docker0/ {print $2}'").read().split('/')[0]
    # minio_host = os.popen("docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' minio-server").read()
    

    # Upload FIle to Minio bucket
    minio_client.put_object(
        bucket_name=f'{bucket_name}',
        object_name=f'input_files/{input_filename}',
        data=image.file,
        length=-1,  # Unknown size, read till EOF,
        part_size=5 << 20 # 5MB chunks
    )

    queue = Queue(queue_name, connection=redis_client)
    job = queue.enqueue(
        'no_prune.main.srgan',
        input_filename,
        node_worker,
        start_timestamp
    )
    
    return job.get_id()
    

async def random_unstructured(image: UploadFile = File(), filename: str = Form(), prune_amount: int = Form(), node_worker: str = Form(), queue_name : str = Form(), start_timestamp : str = Form()):
    input_filename = f'{filename}_random_unstructured_{prune_amount}_{datetime.datetime.now()}{Path(image.filename).suffix}'
    
    # minio_host = os.popen("ip addr | awk '/inet/ && /eno1/ {print $2}'").read().split('/')[0]
    # minio_host = os.popen("ip addr | awk '/inet/ && /wlo1/ {print $2}'").read().split('/')[0]
    # ip_host = node_worker
    # minio_host = os.popen("docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' minio-server").read()
    # ip_host = os.popen("ip addr | awk '/inet/ && /docker0/ {print $2}'").read().split('/')[0]

    # Upload FIle to Minio bucket
    minio_client.put_object(
        bucket_name=f'{bucket_name}',
        object_name=f'input_files/{input_filename}',
        data=image.file,
        length=-1,  # Unknown size, read till EOF,
        part_size=5 << 20 # 5MB chunks
    )

    queue = Queue(queue_name, connection=redis_client)
    job = queue.enqueue(
        'random_unstructured.main.srgan',
        input_filename,
        node_worker,
        start_timestamp,
        prune_amount
    )
    
    return job.get_id()


async def l1_norm(image: UploadFile = File(), filename: str = Form(), prune_amount: int = Form(), node_worker: str = Form(), queue_name : str = Form(), start_timestamp : str = Form()):
    input_filename = f'{filename}_l1_norm_{prune_amount}_{datetime.datetime.now()}{Path(image.filename).suffix}'
    
    # minio_host = os.popen("ip addr | awk '/inet/ && /eno1/ {print $2}'").read().split('/')[0]
    # minio_host = os.popen("ip addr | awk '/inet/ && /wlo1/ {print $2}'").read().split('/')[0]
    # ip_host = node_worker
    # minio_host = os.popen("docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' minio-server").read()
    # ip_host = os.popen("ip addr | awk '/inet/ && /docker0/ {print $2}'").read().split('/')[0]

    # Upload FIle to Minio bucket
    minio_client.put_object(
        bucket_name=f'{bucket_name}',
        object_name=f'input_files/{input_filename}',
        data=image.file,
        length=-1,  # Unknown size, read till EOF,
        part_size=5 << 20 # 5MB chunks
    )

    queue = Queue(queue_name, connection=redis_client)
    job = queue.enqueue(
        'l1_norm.main.srgan',
        input_filename,
        node_worker,
        start_timestamp,
        prune_amount
    )

    return job.get_id()


async def l2_norm(image: UploadFile = File(), filename: str = Form(), prune_amount: int = Form(), node_worker: str = Form(), queue_name : str = Form(), start_timestamp : str = Form()):
    input_filename = f'{filename}_l2_norm_{prune_amount}_{datetime.datetime.now()}{Path(image.filename).suffix}'
    
    # minio_host = os.popen("ip addr | awk '/inet/ && /eno1/ {print $2}'").read().split('/')[0]
    # minio_host = os.popen("ip addr | awk '/inet/ && /wlo1/ {print $2}'").read().split('/')[0]
    # ip_host = node_worker
    # minio_host = os.popen("docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' minio-server").read()
    # ip_host = os.popen("ip addr | awk '/inet/ && /docker0/ {print $2}'").read().split('/')[0]

    # Upload FIle to Minio bucket
    minio_client.put_object(
        bucket_name=f'{bucket_name}',
        object_name=f'input_files/{input_filename}',
        data=image.file,
        length=-1,  # Unknown size, read till EOF,
        part_size=5 << 20 # 5MB chunks
    )

    queue = Queue(queue_name, connection=redis_client)
    job = queue.enqueue(
        'l2_norm.main.srgan',
        input_filename,
        node_worker,
        start_timestamp,
        prune_amount
    )

    return job.get_id()


async def vram_logs(filename: str = Form(), start_timestamp: str = Form(), image_filename: str = Form(), tipe_model: str = Form(), ip_host_manager: str = Form()):
    vram_log = os.popen('nvidia-smi').read()

    gsheet_client = gspread.Client(Credentials.from_authorized_user_file(TOKEN_LOCATION, SCOPES))
    spreadsheet = gsheet_client.open_by_url('https://docs.google.com/spreadsheets/d/1PaFime-HZc-U9Zt3MwzZLolC5BMQWTauUuqZ_JRNIhI/edit#gid=0')
    sheet = spreadsheet.get_worksheet(0)
    sheet.append_row([f'http://localhost:9000/super-resolution/input_files/{image_filename}',
                      f'http://localhost:9000/super-resolution/output_files/{image_filename}',
                      f'http://localhost:9000/super-resolution/vram_logs/{filename}',
                      start_timestamp, requests.get(f'http://{ip_host_manager}:8001/get_current_datetime').text[1:-1], tipe_model, NODE_WORKER])
    
    minio_client.put_object(
        bucket_name=bucket_name,
        object_name=f'vram_logs/{filename}',
        data=BytesIO(bytes(vram_log, 'utf-8')),
        length=len(vram_log)
    )
    return vram_log 


async def get_current_datetime():
    return datetime.datetime.now()
