from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    url: str

    model_config = SettingsConfigDict(env_file="app/.env")