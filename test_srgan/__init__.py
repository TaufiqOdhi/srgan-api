from fastapi.testclient import TestClient
from main import app

base_dir = 'test_srgan/input_image'
client = TestClient(app)
worker_list = [
    # ('192.168.111.83', 'default'), # ip other access point
    # ('10.100.16.142', 'default'), # ip wifi its
    # ('10.21.87.149', 'default'), # ip lan lab pasca
    ('10.21.74.215', 'default'), # ip lan lab ncc
    # ('10.21.87.160', 'ncc-pc-3'),
    ('10.21.87.236', 'lab-pasca-pc-1'),
    ('10.21.74.219', 'ncc-lab-pc-8'),
    ('10.21.74.216', 'ncc-pc-4'),
    # ('192.168.100.254', 'odhi-pc'),
]

