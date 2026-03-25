from enum import Enum

from pydantic import Field
from pydantic_settings import SettingsConfigDict

from app.config.base import BaseAppSettings


class Env(str, Enum):
    DEV = "dev"
    TEST = "test"
    PROD = "prod"


class AppSettings(BaseAppSettings):
    name: str = Field(default="python_web")
    title: str = Field(default="python web")
    env: Env = Field(default=Env.DEV)
    debug: bool = Field(default=True)
    version: str = Field(default="0.0.1")
    description: str = Field(default="A python_web demo.")

    model_config = SettingsConfigDict(
        env_prefix="APP_",
    )