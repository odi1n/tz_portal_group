from functools import lru_cache

from pydantic import BaseSettings, Field, validator


class Settings(BaseSettings):
    server_host: str = Field("localhost")
    server_port: int = Field(8000)


setting = Settings()
