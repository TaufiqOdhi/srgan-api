from fastapi.testclient import TestClient
from main import app

base_dir = 'test_srgan/input_image'
client = TestClient(app)
