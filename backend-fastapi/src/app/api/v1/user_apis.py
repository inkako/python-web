from fastapi import APIRouter
from starlette.responses import JSONResponse

from app.schema.api_response import Fail, Success
from app.schema.user_schemas import UserCreate
from app.service import user_service

router = APIRouter(prefix="/user", tags=["用户模块"])


@router.post("/create", summary="创建用户")
async def create_user(user_in: UserCreate) -> JSONResponse:
    user = await user_service.get_by_username(user_in.username)
    if user:
        return Fail(msg="用户已存在")
    await user_service.create_user(user_in)
    return Success(msg="创建成功")
