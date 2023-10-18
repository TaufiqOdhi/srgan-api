from minio import Minio
from datetime import timedelta


#Initialize Minio Client
minio_client = Minio(
    endpoint="localhost:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False, # disable SSL
)

bucket_name = "super-resolution"


# url = minio_client.presigned_get_object(
#     bucket_name=bucket_name,
#     object_name='input_files/0805x4.png',
#     expires=timedelta(days=1)
# )
# print(url)