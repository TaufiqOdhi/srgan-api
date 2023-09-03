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
    '/l1_norm_30',
    l1_norm_30,
    methods=['post'],
    tags=['srgan'],
    # response_class=FileResponse
)

main_router.add_api_route(
    '/l1_norm_50',
    l1_norm_50,
    methods=['post'],
    tags=['srgan'],
    # response_class=FileResponse
)

main_router.add_api_route(
    '/l1_norm_70',
    l2_norm_70,
    methods=['post'],
    tags=['srgan'],
    # response_class=FileResponse
)

main_router.add_api_route(
    '/l2_norm_30',
    l2_norm_30,
    methods=['post'],
    tags=['srgan'],
    # response_class=FileResponse
)

main_router.add_api_route(
    '/l2_norm_50',
    l2_norm_50,
    methods=['post'],
    tags=['srgan'],
    # response_class=FileResponse
)

main_router.add_api_route(
    '/l2_norm_70',
    l2_norm_70,
    methods=['post'],
    tags=['srgan'],
    # response_class=FileResponse
)
