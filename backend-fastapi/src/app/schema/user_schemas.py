from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    username: str = Field(..., min_length=1, max_length=32, examples=["admin"])
    password: str = Field(..., min_length=6, max_length=128, examples=["123456"])
    email: str = Field(..., min_length=1, max_length=255, examples=["admin@example.com"])
    is_active: bool = Field(default=True)
    is_superuser: bool = Field(default=False)


class UserUpdate(BaseModel):
    ...