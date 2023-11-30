import subprocess
import os
import datetime
from fastapi import Form


def _scale_up(service_name, num_scale=1):
    command = f"docker service ps {service_name}"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, text=True)
    list_lines = []
    for line in process.stdout:
        list_lines.append(line.strip())
    curr_scale = len(list_lines[1:])
    os.system(f"docker service scale {service_name}={curr_scale+num_scale}")


def _scale_down(service_name, target_scale=1):
    os.system(f"docker service scale {service_name}={target_scale}")


async def scale_check(start_timestamp: str = Form(), finish_timestamp: str = Form()):
    finish_timestamp = datetime.datetime.strptime(finish_timestamp, '%Y-%m-%d %H:%M:%S.%f')
    start_timestamp = datetime.datetime.strptime(start_timestamp, '%Y-%m-%d %H:%M:%S.%f')
    time_processing = finish_timestamp - start_timestamp
    if time_processing > datetime.timedelta(seconds=10):
        print('mau scale up')
        _scale_up(service_name='srgan-worker-2_all')
    else:
       print(f'belum mau scale up, karena time processing : {time_processing}')
       pass
    #    _scale_down(service_name='srgan-worker-2_all', target_scale=1) 
