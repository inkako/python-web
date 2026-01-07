from typing import Generic, TypeVar, Type

from pydantic import BaseModel
from tortoise import Model

ModelType = TypeVar("ModelType", bound=Model)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CrudBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def create(self, obj_in: CreateSchemaType):
        ...

    async def retrieve(self, mid: int) -> ModelType:
        return await self.model.get(id=mid)


