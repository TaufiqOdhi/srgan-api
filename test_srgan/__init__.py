from fastapi.testclient import TestClient
from main import app

base_dir = 'test_srgan/input_image'
client = TestClient(app)
worker_list = [
    # ('10.100.16.142', 'default'), 
    # ('192.168.100.102', 'default'),
    ('10.21.87.149', 'default'),
    ('10.21.87.160', 'ncc-pc-3'),
    ('10.21.87.236', 'lab-pasca-pc-1'),
    ('10.21.74.219', 'ncc-lab-pc-8'),
    ('10.21.74.216', 'ncc-pc-4'),
    # ('192.168.100.254', 'odhi-pc'),
]

