from typing import Generic, TypeVar, Type, Tuple, Dict, Any

from pydantic import BaseModel
from tortoise import Model
from tortoise.expressions import Q

ModelType = TypeVar("ModelType", bound=Model)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CrudBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def create(self, obj_in: CreateSchemaType | Dict[str, Any]) -> ModelType:
        if isinstance(obj_in, dict):
            obj_dict = obj_in
        else:
            obj_dict = obj_in.model_dump()
        obj: Model = self.model(**obj_dict)
        await obj.save()
        return obj

    async def retrieve(self, mid: int) -> ModelType:
        return await self.model.get(id=mid)

    async def list(self, page: int, rows: int, order=None, search: Q = Q()) -> Tuple[int, list[ModelType]]:
        """
        Retrieve a paginated and ordered list of model instances.

        Summary:
        This function fetches a subset of model instances from the database, based on the provided page number, number of rows per page, order, and search criteria.
        The results are paginated and can be sorted by specifying the order. It also returns the total count of items matching the search criteria.

        Args:
            page (int): The page number to fetch.
            rows (int): The number of rows per page.
            order (list, optional): A list of fields to order the results by. Defaults to an empty list.
            search (Q, optional): A Q object representing the search query. Defaults to an empty Q object.

        Returns:
            Tuple[int, list[ModelType]]: A tuple containing the total count of items and the list of model instances for the specified page.

        Raises:
            None
        """
        query_set = self.model.filter(search)
        return await query_set.count(), await query_set.offset((page - 1) * rows).limit(rows).order_by(*order if order is not None else [])

    async def update(self, mid: int, obj_in: UpdateSchemaType | Dict[str, Any]) -> ModelType:
        if isinstance(obj_in, dict):
            obj_dict = obj_in
        else:
            obj_dict = obj_in.model_dump()
        obj = await self.retrieve(mid)
        obj.update_from_dict(obj_dict)
        await obj.save()
        return obj

    async def delete(self, mid: int) -> None:
        obj = await self.retrieve(mid)
        await obj.delete()
