from test_srgan import client, base_dir, worker_list
import os
import datetime


srgan_enpoint = '/no_prune'
node_worker, queue_name = worker_list[0]


def test_no_prune_1():
    filename = '1'
    res = client.post(
        srgan_enpoint,
        data=dict(filename=filename, node_worker=node_worker, queue_name=queue_name, start_timestamp=datetime.datetime.now().__str__()),
        files=dict(image=open(f'{base_dir}/{filename}.png', 'rb'))
    )
    assert res.status_code == 200
    # assert not res.json().get('error')
    # os.system(f'nvidia-smi > "vram_logs/no_prune/vram_consumption_{filename}_noPrune_{datetime.datetime.now()}.txt"')

def test_no_prune_2():
    filename = '2'
    res = client.post(
        srgan_enpoint,
        data=dict(filename=filename, node_worker=node_worker, queue_name=queue_name, start_timestamp=datetime.datetime.now().__str__()),
        files=dict(image=open(f'{base_dir}/{filename}.png', 'rb'))
    )
    assert res.status_code == 200
    # assert not res.json().get('error')
    # os.system(f'nvidia-smi > "vram_logs/no_prune/vram_consumption_{filename}_noPrune_{datetime.datetime.now()}.txt"')

def test_no_prune_3():
    filename = '3'
    res = client.post(
        srgan_enpoint,
        data=dict(filename=filename, node_worker=node_worker, queue_name=queue_name, start_timestamp=datetime.datetime.now().__str__()),
        files=dict(image=open(f'{base_dir}/{filename}.png', 'rb'))
    )
    assert res.status_code == 200
    # assert not res.json().get('error')
    # os.system(f'nvidia-smi > "vram_logs/no_prune/vram_consumption_{filename}_noPrune_{datetime.datetime.now()}.txt"')

def test_no_prune_4():
    filename = '4'
    res = client.post(
        srgan_enpoint,
        data=dict(filename=filename, node_worker=node_worker, queue_name=queue_name, start_timestamp=datetime.datetime.now().__str__()),
        files=dict(image=open(f'{base_dir}/{filename}.png', 'rb'))
    )
    assert res.status_code == 200
    # assert not res.json().get('error')
    # os.system(f'nvidia-smi > "vram_logs/no_prune/vram_consumption_{filename}_noPrune_{datetime.datetime.now()}.txt"')

def test_no_prune_5():
    filename = '5'
    res = client.post(
        srgan_enpoint,
        data=dict(filename=filename, node_worker=node_worker, queue_name=queue_name, start_timestamp=datetime.datetime.now().__str__()),
        files=dict(image=open(f'{base_dir}/{filename}.png', 'rb'))
    )
    assert res.status_code == 200
    # assert not res.json().get('error')
    # os.system(f'nvidia-smi > "vram_logs/no_prune/vram_consumption_{filename}_noPrune_{datetime.datetime.now()}.txt"')

def test_no_prune_6():
    filename = '6'
    res = client.post(
        srgan_enpoint,
        data=dict(filename=filename, node_worker=node_worker, queue_name=queue_name, start_timestamp=datetime.datetime.now().__str__()),
        files=dict(image=open(f'{base_dir}/{filename}.png', 'rb'))
    )
    assert res.status_code == 200
    # assert not res.json().get('error')
    # os.system(f'nvidia-smi > "vram_logs/no_prune/vram_consumption_{filename}_noPrune_{datetime.datetime.now()}.txt"')
