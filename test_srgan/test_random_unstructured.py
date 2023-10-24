from test_srgan import client, base_dir
import os
import datetime


srgan_enpoint = '/random_unstructured'


def test_random_unstructured_1():
    filename = '1'
    prune_amount = 30
    res = client.post(
        srgan_enpoint,
        data=dict(filename=filename, prune_amount=prune_amount),
        files=dict(image=open(f'{base_dir}/{filename}.png', 'rb'))
    )
    assert res.status_code == 200
    # os.system(f'nvidia-smi > "vram_logs/random_unstructured/vram_consumption_{filename}_{prune_amount}randomUnstructured_{datetime.datetime.now()}.txt"')

def test_random_unstructured_2():
    filename = '2'
    prune_amount = 50
    res = client.post(
        srgan_enpoint,
        data=dict(filename=filename, prune_amount=prune_amount),
        files=dict(image=open(f'{base_dir}/{filename}.png', 'rb'))
    )
    assert res.status_code == 200
    # os.system(f'nvidia-smi > "vram_logs/random_unstructured/vram_consumption_{filename}_{prune_amount}randomUnstructured_{datetime.datetime.now()}.txt"')

def test_random_unstructured_3():
    filename = '3'
    prune_amount = 70
    res = client.post(
        srgan_enpoint,
        data=dict(filename=filename, prune_amount=prune_amount),
        files=dict(image=open(f'{base_dir}/{filename}.png', 'rb'))
    )
    assert res.status_code == 200
    # os.system(f'nvidia-smi > "vram_logs/random_unstructured/vram_consumption_{filename}_{prune_amount}randomUnstructured_{datetime.datetime.now()}.txt"')

def test_random_unstructured_4():
    filename = '4'
    prune_amount = 30
    res = client.post(
        srgan_enpoint,
        data=dict(filename=filename, prune_amount=prune_amount),
        files=dict(image=open(f'{base_dir}/{filename}.png', 'rb'))
    )
    assert res.status_code == 200
    # os.system(f'nvidia-smi > "vram_logs/random_unstructured/vram_consumption_{filename}_{prune_amount}randomUnstructured_{datetime.datetime.now()}.txt"')

def test_random_unstructured_5():
    filename = '5'
    prune_amount = 50
    res = client.post(
        srgan_enpoint,
        data=dict(filename=filename, prune_amount=prune_amount),
        files=dict(image=open(f'{base_dir}/{filename}.png', 'rb'))
    )
    assert res.status_code == 200
    # os.system(f'nvidia-smi > "vram_logs/random_unstructured/vram_consumption_{filename}_{prune_amount}randomUnstructured_{datetime.datetime.now()}.txt"')

def test_random_unstructured_6():
    filename = '6'
    prune_amount = 70
    res = client.post(
        srgan_enpoint,
        data=dict(filename=filename, prune_amount=prune_amount),
        files=dict(image=open(f'{base_dir}/{filename}.png', 'rb'))
    )
    assert res.status_code == 200
    # os.system(f'nvidia-smi > "vram_logs/random_unstructured/vram_consumption_{filename}_{prune_amount}randomUnstructured_{datetime.datetime.now()}.txt"')
