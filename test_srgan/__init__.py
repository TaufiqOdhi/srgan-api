from fastapi.testclient import TestClient
from main import app

base_dir = 'test_srgan/input_image'
client = TestClient(app)
worker_list = [
    # ('10.21.87.149', 'default'),
    ('10.100.16.142', 'default'), 
    ('10.21.87.160', 'ncc-pc-3')
]

