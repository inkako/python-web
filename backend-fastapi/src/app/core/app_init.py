import shutil

from aerich import Command
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError, ResponseValidationError
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware

from app.api import v1_router
from app.config import TORTOISE_ORM
from app.core.exception_handlers import HttpExceptionHandler, RequestValidationHandler


# from app.logging import logger


async def init_db():
    """ 数据库初始化 """
    command = Command(tortoise_config = TORTOISE_ORM)
    try:
        # 创建初始表结构
        await command.init_db(safe=True)
    except FileExistsError:
        pass
    # 初始化迁移环境
    await command.init()
    try:
        # 生成迁移文件
        await command.migrate()
    except AttributeError:
        # logger.warning("unable to retrieve models history from db, models history will be created from scratch")
        shutil.rmtree("migrations")
        await command.init_db(safe=True)
    # 应用迁移
    await command.upgrade(run_in_transaction=True)


async def init_data():
    """ 初始化 """
    await init_db()


def add_middlewares(app: FastAPI):
    """ 添加中间件 """
    app.add_middleware(CORSMiddleware,
                       allow_origins=["*"],
                       allow_credentials=True,
                       allow_methods=["*"],
                       allow_headers=["*"])


def add_routers(app: FastAPI):
    """ 添加路由 """
    app.include_router(v1_router)


def add_exception_handlers(app: FastAPI):
    """ 添加异常处理 """
    app.add_exception_handler(HTTPException, HttpExceptionHandler)
    app.add_exception_handler(RequestValidationError, RequestValidationHandler)
    app.add_exception_handler(ResponseValidationError, ResponseValidationError)
