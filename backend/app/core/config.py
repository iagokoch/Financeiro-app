from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # procura no arquivo .env
    DATABASE_URL: str
    DEBUG: bool
    APP_ENV: str
    JWT_SECRET: str
    ACESS_TOKEN_EXPIRE_MINUTES: int

    # puxa do .env essas variaveis
    model_config = SettingsConfigDict(env_file=".env")

    # instancia as configs
    config = Settings()
