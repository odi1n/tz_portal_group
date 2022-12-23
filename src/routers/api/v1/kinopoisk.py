from fastapi import APIRouter

from src.utils.kinopoisk import get_infomation, Movie

router_kinopoisk = APIRouter(prefix="/kinopoisk", tags=['kinopoisk'])


@router_kinopoisk.get("/", response_model=Movie)
async def get() -> Movie:
    return await get_infomation()
