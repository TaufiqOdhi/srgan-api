from fastapi import APIRouter
from fastapi.responses import FileResponse
from endpoints.super_resolution import *

main_router = APIRouter()

main_router.add_api_route(
    '/no_prune',
    no_prune,
    methods=['post'],
    tags=['srgan'],
    # response_class=FileResponse
)

main_router.add_api_route(
    '/random_unstructured/30',
    random_unstructured_30,
    methods=['post'],
    tags=['srgan'],
    # response_class=FileResponse
)

main_router.add_api_route(
    '/random_unstructured/50',
    random_unstructured_50,
    methods=['post'],
    tags=['srgan'],
    # response_class=FileResponse
)

main_router.add_api_route(
    '/random_unstructured/70',
    random_unstructured_70,
    methods=['post'],
    tags=['srgan'],
    # response_class=FileResponse
)

main_router.add_api_route(
    '/l1_norm',
    l1_norm,
    methods=['post'],
    tags=['srgan'],
    response_class=FileResponse
)

main_router.add_api_route(
    '/l2_norm',
    l2_norm,
    methods=['post'],
    tags=['srgan'],
    response_class=FileResponse
)
