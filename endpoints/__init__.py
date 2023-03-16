from fastapi import APIRouter
from fastapi.responses import FileResponse
from endpoints.super_resolution import no_prune, random_unstructured, l1_norm, l2_norm

main_router = APIRouter()

main_router.add_api_route(
    '/no_prune',
    no_prune,
    methods=['post'],
    tags=['srgan'],
    response_class=FileResponse
)

main_router.add_api_route(
    '/random_unstructured',
    random_unstructured,
    methods=['post'],
    tags=['srgan'],
    response_class=FileResponse
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
