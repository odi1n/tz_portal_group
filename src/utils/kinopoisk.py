import asyncio
from typing import List

import aiohttp
from pydantic import BaseModel

from src.settings import setting

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


async def get_infomation() -> Movie:
    params = {
        'field': "top250",
        "search": "!null",
        "selectField": "id name top250",
        "limit": "5",
        "token": setting.token_kinopoisk_dev,
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(LINK_MOVIE, params=params) as response:
            json_Data = await response.json()
            return Movie(**json_Data)


if __name__ == "__main__":
    asyncio.run(get_infomation())
