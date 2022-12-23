from fastapi import APIRouter

from .kinopoisk import router_kinopoisk
from .numbers import router_number

router_v1 = APIRouter(prefix="/v1")
router_v1.include_router(router_number)
router_v1.include_router(router_kinopoisk)
