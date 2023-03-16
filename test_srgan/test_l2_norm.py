from test_srgan import client, base_dir
import os
import datetime


srgan_enpoint = '/l2_norm'


def test_l2_norm_1():
    filename = '1'
    res = client.post(
        srgan_enpoint,
        data=dict(filename=filename, prune_amount=30),
        files=dict(image=open(f'{base_dir}/{filename}.png', 'rb'))
    )
    assert res.status_code == 200
    os.system(f'nvidia-smi > "vram_logs/l2_norm/vram_consumption_{filename}_randomUnstructured_{datetime.datetime.now()}.txt"')

def test_l2_norm_2():
    filename = '2'
    res = client.post(
        srgan_enpoint,
        data=dict(filename=filename, prune_amount=50),
        files=dict(image=open(f'{base_dir}/{filename}.png', 'rb'))
    )
    assert res.status_code == 200
    os.system(f'nvidia-smi > "vram_logs/l2_norm/vram_consumption_{filename}_randomUnstructured_{datetime.datetime.now()}.txt"')

def test_l2_norm_3():
    filename = '3'
    res = client.post(
        srgan_enpoint,
        data=dict(filename=filename, prune_amount=70),
        files=dict(image=open(f'{base_dir}/{filename}.png', 'rb'))
    )
    assert res.status_code == 200
    os.system(f'nvidia-smi > "vram_logs/l2_norm/vram_consumption_{filename}_randomUnstructured_{datetime.datetime.now()}.txt"')

def test_l2_norm_4():
    filename = '4'
    res = client.post(
        srgan_enpoint,
        data=dict(filename=filename, prune_amount=30),
        files=dict(image=open(f'{base_dir}/{filename}.png', 'rb'))
    )
    assert res.status_code == 200
    os.system(f'nvidia-smi > "vram_logs/l2_norm/vram_consumption_{filename}_randomUnstructured_{datetime.datetime.now()}.txt"')

def test_l2_norm_5():
    filename = '5'
    res = client.post(
        srgan_enpoint,
        data=dict(filename=filename, prune_amount=50),
        files=dict(image=open(f'{base_dir}/{filename}.png', 'rb'))
    )
    assert res.status_code == 200
    os.system(f'nvidia-smi > "vram_logs/l2_norm/vram_consumption_{filename}_randomUnstructured_{datetime.datetime.now()}.txt"')

def test_l2_norm_6():
    filename = '6'
    res = client.post(
        srgan_enpoint,
        data=dict(filename=filename, prune_amount=70),
        files=dict(image=open(f'{base_dir}/{filename}.png', 'rb'))
    )
    assert res.status_code == 200
    os.system(f'nvidia-smi > "vram_logs/l2_norm/vram_consumption_{filename}_randomUnstructured_{datetime.datetime.now()}.txt"')
