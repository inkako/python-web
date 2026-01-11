from pydantic import Field
from pydantic_settings import BaseSettings


class DatabaseSettings(BaseSettings):
    host: str = Field(default="localhost")
    port: int = Field(default=3306)
    username: str = Field(default="root")
    password: str = Field(default="123456")
    database: str = Field(default="python_web")

