from test_srgan import client, base_dir
import os
import datetime


srgan_enpoint = '/l1_norm'


def test_l1_norm_1():
    filename = '1'
    prune_amount = 30
    res = client.post(
        srgan_enpoint,
        data=dict(filename=filename, prune_amount=prune_amount),
        files=dict(image=open(f'{base_dir}/{filename}.png', 'rb'))
    )
    assert res.status_code == 200
    # os.system(f'nvidia-smi > "vram_logs/l1_norm/vram_consumption_{filename}_{prune_amount}l1Norm_{datetime.datetime.now()}.txt"')

def test_l1_norm_2():
    filename = '2'
    prune_amount = 50
    res = client.post(
        srgan_enpoint,
        data=dict(filename=filename, prune_amount=prune_amount),
        files=dict(image=open(f'{base_dir}/{filename}.png', 'rb'))
    )
    assert res.status_code == 200
    # os.system(f'nvidia-smi > "vram_logs/l1_norm/vram_consumption_{filename}_{prune_amount}l1Norm_{datetime.datetime.now()}.txt"')

def test_l1_norm_3():
    filename = '3'
    prune_amount = 70
    res = client.post(
        srgan_enpoint,
        data=dict(filename=filename, prune_amount=prune_amount),
        files=dict(image=open(f'{base_dir}/{filename}.png', 'rb'))
    )
    assert res.status_code == 200
    # os.system(f'nvidia-smi > "vram_logs/l1_norm/vram_consumption_{filename}_{prune_amount}l1Norm_{datetime.datetime.now()}.txt"')

def test_l1_norm_4():
    filename = '4'
    prune_amount = 30
    res = client.post(
        srgan_enpoint,
        data=dict(filename=filename, prune_amount=prune_amount),
        files=dict(image=open(f'{base_dir}/{filename}.png', 'rb'))
    )
    assert res.status_code == 200
    # os.system(f'nvidia-smi > "vram_logs/l1_norm/vram_consumption_{filename}_{prune_amount}l1Norm_{datetime.datetime.now()}.txt"')

def test_l1_norm_5():
    filename = '5'
    prune_amount = 50
    res = client.post(
        srgan_enpoint,
        data=dict(filename=filename, prune_amount=prune_amount),
        files=dict(image=open(f'{base_dir}/{filename}.png', 'rb'))
    )
    assert res.status_code == 200
    # os.system(f'nvidia-smi > "vram_logs/l1_norm/vram_consumption_{filename}_{prune_amount}l1Norm_{datetime.datetime.now()}.txt"')

def test_l1_norm_6():
    filename = '6'
    prune_amount = 70
    res = client.post(
        srgan_enpoint,
        data=dict(filename=filename, prune_amount=prune_amount),
        files=dict(image=open(f'{base_dir}/{filename}.png', 'rb'))
    )
    assert res.status_code == 200
    # os.system(f'nvidia-smi > "vram_logs/l1_norm/vram_consumption_{filename}_{prune_amount}l1Norm_{datetime.datetime.now()}.txt"')
