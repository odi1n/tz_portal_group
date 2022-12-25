import asyncio
from typing import List, Union

import aiohttp
from pydantic import BaseModel

from settings import setting

LINK_MOVIE = "https://api.kinopoisk.dev/movie"


class MovieModel(BaseModel):
    id: int
    name: str


class Page(BaseModel):
    total: int
    limit: int
    page: int
    pages: int


class Movie(Page):
    docs: List[MovieModel]


class RequestError(BaseModel):
    message: str


async def get_information() -> Union[Movie, RequestError]:
    params = {
        'field': "top250",
        "search": "!null",
        "selectField": "id name top250",
        "limit": "5",
        "token": setting.token_kinopoisk_dev,
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(LINK_MOVIE, params=params) as response:
            data_json = await response.json()
            if response.status == 200:
                return Movie(**data_json)
            return RequestError(**data_json)
