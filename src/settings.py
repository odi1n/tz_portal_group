from functools import lru_cache

from pydantic import BaseSettings, Field, validator


class Settings(BaseSettings):
    class Config:
        env_prefix = ""
        case_sensitive = False
        env_file = '.env'
        env_file_encoding = 'utf-8'

    server_host: str = Field("localhost")
    server_port: int = Field(8000)

    token_kinopoisk_dev: str = None


@lru_cache()
def get_settings():
    return Settings()


setting = get_settings()

print(setting.token_kinopoisk_dev)
