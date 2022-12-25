from functools import lru_cache

from pydantic import BaseSettings, Field, validator


class Settings(BaseSettings):
    class Config:
        env_prefix = ""
        case_sensitive = False
        env_file = '.env'
        env_file_encoding = 'utf-8'

    server_host: str
    server_port: int

    token_kinopoisk_dev: str = None

    access_token_expire_minutes: int = 30  # 30 min
    refresh_token_expire_minutes: int = 60 * 24 * 7  # 7 day
    algorithm: str = "HS256"
    jwt_secret_key: str
    jwt_refresh_secret_key: str

    postgres_db: str = "db"
    postgres_user: str = "user"
    postgres_password: str = "pass"
    postgres_host: str = "localhost"
    postgres_port: int = 5432
    db_url: str = None

    @validator('db_url')
    def db_url_path(cls, v, values: dict) -> dict:
        return f"postgres://{values.get('postgres_user')}:{values.get('postgres_password')}" \
               f"@{values.get('postgres_host')}:{values.get('postgres_port')}/{values.get('postgres_db')}"


@lru_cache()
def get_settings():
    return Settings()


setting = get_settings()

TORTOISE_ORM = {
    "connections": {"default": setting.db_url},
    "apps": {
        "models": {
            "models": ["src.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}
