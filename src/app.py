from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from src.routers import router
from src.settings import setting

app = FastAPI(
    title="Tz portal group",
    version="0.1.0",
    description="Description api",
)
app.include_router(router)

register_tortoise(
    app,
    db_url=setting.db_url,
    modules={"models": ["src.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)