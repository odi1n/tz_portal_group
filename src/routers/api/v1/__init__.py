from fastapi import APIRouter

from .kinopoisk import router_kinopoisk
from .numbers import router_number
from .user import router_user

router_v1 = APIRouter(prefix="/v1")
router_v1.include_router(router_number)
router_v1.include_router(router_kinopoisk)
router_v1.include_router(router_user)
