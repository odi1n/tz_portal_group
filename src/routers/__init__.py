from fastapi import APIRouter
from .api import router_api
from .page import router_page
from .websocket import router_ws

router = APIRouter()
router.include_router(router_page)
router.include_router(router_ws)
router.include_router(router_api)
