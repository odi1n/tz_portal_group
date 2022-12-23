from fastapi import FastAPI
from api import router_api

app = FastAPI()
app.include_router(router_api)
