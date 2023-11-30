import datetime
import os
from io import BytesIO
from minio_connection import minio_client, bucket_name

async def get_current_datetime():
    return datetime.datetime.now().__str__()


async def current_worker_logs(filename: str, stack_name: str = 'srgan-worker'):
    curr_worker = os.popen(f'docker stack ps {stack_name}').read()

    minio_client.put_object(
        bucket_name=bucket_name,
        object_name=f'current_worker/{filename}',
        data=BytesIO(bytes(curr_worker, 'utf-8')),
        length=len(curr_worker)
    )
    return curr_worker
