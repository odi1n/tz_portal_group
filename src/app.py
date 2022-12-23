from fastapi import FastAPI

from api import router_api
from page import router_app
from websocket import router_ws

app = FastAPI(
    title="Tz portal group",
    version="0.1.0",
    description="Description api",
)
app.include_router(router_app)
app.include_router(router_ws)
app.include_router(router_api)

