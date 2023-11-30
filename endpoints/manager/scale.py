import subprocess
import os
import datetime
from fastapi import Form


def scale_up(service_name, num_scale=1):
    command = f"docker service ps {service_name}"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, text=True)
    list_lines = []
    for line in process.stdout:
        list_lines.append(line.strip())
    curr_scale = len(list_lines[1:])
    os.system(f"docker service scale {service_name}={curr_scale+num_scale}")


def scale_down(service_name, target_scale=1):
    os.system(f"docker service scale {service_name}={target_scale}")


async def scale_check(time_processing: str = Form()):
    time_processing = datetime.datetime.strptime(time_processing, '%H:%M:%S.%f').timestamp()
    if time_processing > datetime.timedelta(seconds=10).total_seconds():
        scale_up(service_name='srgan-worker-2_all')
    else:
       pass
    #    scale_down(service_name='srgan-worker-2_all', target_scale=1) 
