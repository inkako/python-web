from pydantic import Field
from pydantic_settings import SettingsConfigDict

from app.config.base import BaseAppSettings


class LoggingSettings(BaseAppSettings):
    debug: bool = Field(default=False)
    level: str = Field(default="INFO")

    model_config = SettingsConfigDict(
        env_prefix="LOG_"
    )
