from fastapi import APIRouter
from endpoints.super_resolution import no_prune, random_unstructured, l1_norm, l2_norm, vram_logs
from endpoints.manager import get_current_datetime, current_worker_logs
from endpoints.manager.scale import scale_check

main_router = APIRouter()

main_router.add_api_route(
    '/no_prune',
    no_prune,
    methods=['post'],
    tags=['srgan'],
)

main_router.add_api_route(
    '/random_unstructured',
    random_unstructured,
    methods=['post'],
    tags=['srgan'],
)

main_router.add_api_route(
    '/l1_norm',
    l1_norm,
    methods=['post'],
    tags=['srgan'],
)

main_router.add_api_route(
    '/l2_norm',
    l2_norm,
    methods=['post'],
    tags=['srgan'],
)

main_router.add_api_route(
    '/vram_logs',
    vram_logs,
    methods=['post'],
    tags=['logs'],
)

main_router.add_api_route(
    '/get_current_datetime',
    get_current_datetime,
    methods=['get'],
    tags=['logs']
)

main_router.add_api_route(
    '/current_worker_logs',
    current_worker_logs,
    methods=['get'],
    tags=['logs']
)

main_router.add_api_route(
    '/scale_check',
    scale_check,
    methods=['post'],
    tags=['management']
)
