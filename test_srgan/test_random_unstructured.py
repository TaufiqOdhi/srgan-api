from test_srgan import client, base_dir, worker_list
import os
import datetime


srgan_endpoint = '/random_unstructured'
node_worker, queue_name = worker_list[0]
# queue_name = 'all'


def test_random_unstructured_1():
    filename = '1'
    prune_amount = 30
    res = client.post(
        srgan_endpoint,
        data=dict(filename=filename, prune_amount=prune_amount, node_worker=node_worker, queue_name=queue_name, start_timestamp=datetime.datetime.now().__str__()),
        files=dict(image=open(f'{base_dir}/{filename}.png', 'rb'))
    )
    assert res.status_code == 200
    # assert not res.json().get('error')
    # os.system(f'nvidia-smi > "vram_logs/random_unstructured/vram_consumption_{filename}_{prune_amount}randomUnstructured_{datetime.datetime.now()}.txt"')

def test_random_unstructured_2():
    filename = '2'
    prune_amount = 50
    res = client.post(
        srgan_endpoint,
        data=dict(filename=filename, prune_amount=prune_amount, node_worker=node_worker, queue_name=queue_name, start_timestamp=datetime.datetime.now().__str__()),
        files=dict(image=open(f'{base_dir}/{filename}.png', 'rb'))
    )
    assert res.status_code == 200
    # assert not res.json().get('error')
    # os.system(f'nvidia-smi > "vram_logs/random_unstructured/vram_consumption_{filename}_{prune_amount}randomUnstructured_{datetime.datetime.now()}.txt"')

def test_random_unstructured_3():
    filename = '3'
    prune_amount = 70
    res = client.post(
        srgan_endpoint,
        data=dict(filename=filename, prune_amount=prune_amount, node_worker=node_worker, queue_name=queue_name, start_timestamp=datetime.datetime.now().__str__()),
        files=dict(image=open(f'{base_dir}/{filename}.png', 'rb'))
    )
    assert res.status_code == 200
    # assert not res.json().get('error')
    # os.system(f'nvidia-smi > "vram_logs/random_unstructured/vram_consumption_{filename}_{prune_amount}randomUnstructured_{datetime.datetime.now()}.txt"')

def test_random_unstructured_4():
    filename = '4'
    prune_amount = 30
    res = client.post(
        srgan_endpoint,
        data=dict(filename=filename, prune_amount=prune_amount, node_worker=node_worker, queue_name=queue_name, start_timestamp=datetime.datetime.now().__str__()),
        files=dict(image=open(f'{base_dir}/{filename}.png', 'rb'))
    )
    assert res.status_code == 200
    # assert not res.json().get('error')
    # os.system(f'nvidia-smi > "vram_logs/random_unstructured/vram_consumption_{filename}_{prune_amount}randomUnstructured_{datetime.datetime.now()}.txt"')

def test_random_unstructured_5():
    filename = '5'
    prune_amount = 50
    res = client.post(
        srgan_endpoint,
        data=dict(filename=filename, prune_amount=prune_amount, node_worker=node_worker, queue_name=queue_name, start_timestamp=datetime.datetime.now().__str__()),
        files=dict(image=open(f'{base_dir}/{filename}.png', 'rb'))
    )
    assert res.status_code == 200
    # assert not res.json().get('error')
    # os.system(f'nvidia-smi > "vram_logs/random_unstructured/vram_consumption_{filename}_{prune_amount}randomUnstructured_{datetime.datetime.now()}.txt"')

def test_random_unstructured_6():
    filename = '6'
    prune_amount = 70
    res = client.post(
        srgan_endpoint,
        data=dict(filename=filename, prune_amount=prune_amount, node_worker=node_worker, queue_name=queue_name, start_timestamp=datetime.datetime.now().__str__()),
        files=dict(image=open(f'{base_dir}/{filename}.png', 'rb'))
    )
    assert res.status_code == 200
    # assert not res.json().get('error')
    # os.system(f'nvidia-smi > "vram_logs/random_unstructured/vram_consumption_{filename}_{prune_amount}randomUnstructured_{datetime.datetime.now()}.txt"')
