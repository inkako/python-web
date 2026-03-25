from pydantic import Field
from pydantic_settings import SettingsConfigDict

from app.config.base import BaseAppSettings


class DatabaseSettings(BaseAppSettings):
    host: str = Field(default="127.0.0.1")
    port: int = Field(default=3306)
    username: str = Field(default="root")
    password: str = Field(default="123456")
    database: str = Field(default="python_web")

    model_config = SettingsConfigDict(
        env_prefix="DB_"
    )
