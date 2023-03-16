from test_main import client, base_dir
import os
import datetime

srgan_enpoint = '/no_prune'


def test_no_prune_1():
    filename = '1'
    res = client.post(
        srgan_enpoint,
        data=dict(filename=filename),
        files=dict(image=open(f'{base_dir}/{filename}.png', 'rb'))
    )
    assert res.status_code == 200
    os.system(f'nvidia-smi > "vram_logs/vram_consumption_{filename}_noPrune_{datetime.datetime.now()}.txt"')

def test_no_prune_2():
    filename = '2'
    res = client.post(
        srgan_enpoint,
        data=dict(filename=filename),
        files=dict(image=open(f'{base_dir}/{filename}.png', 'rb'))
    )
    assert res.status_code == 200
    os.system('nvidia-smi > vram_consumption_{}_{}.txt'.format(filename, uuid.uuid4()))

def test_no_prune_3():
    filename = '3'
    res = client.post(
        srgan_enpoint,
        data=dict(filename=filename),
        files=dict(image=open(f'{base_dir}/{filename}.png', 'rb'))
    )
    assert res.status_code == 200
    os.system('nvidia-smi > vram_consumption_{}_{}.txt'.format(filename, uuid.uuid4()))

def test_no_prune_4():
    filename = '4'
    res = client.post(
        srgan_enpoint,
        data=dict(filename=filename),
        files=dict(image=open(f'{base_dir}/{filename}.png', 'rb'))
    )
    assert res.status_code == 200
    os.system('nvidia-smi > vram_consumption_{}_{}.txt'.format(filename, uuid.uuid4()))

def test_no_prune_5():
    filename = '5'
    res = client.post(
        srgan_enpoint,
        data=dict(filename=filename),
        files=dict(image=open(f'{base_dir}/{filename}.png', 'rb'))
    )
    assert res.status_code == 200
    os.system('nvidia-smi > vram_consumption_{}_{}.txt'.format(filename, uuid.uuid4()))
