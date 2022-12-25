from typing import Union

from fastapi import APIRouter, Depends

from src.models import User_Pydantic
from src.service.auth import get_current_user
from src.utils.kinopoisk import get_information, Movie, RequestError

router_kinopoisk = APIRouter(prefix="/kinopoisk", tags=['kinopoisk'])


@router_kinopoisk.get("/", summary="Get kinopoisk top5 movie", response_model=Union[Movie, RequestError])
async def get(
        user: User_Pydantic = Depends(get_current_user)
) -> Movie:
    """
    Get kinopoisk top5 movie
    :param user:
    :return:
    """
    return await get_information()
