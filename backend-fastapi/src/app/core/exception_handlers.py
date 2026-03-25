from http import HTTPStatus

from fastapi.exceptions import RequestValidationError, ResponseValidationError
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse


def HttpExceptionHandler(_: Request, exc: HTTPException) -> JSONResponse:
    content = dict(code=exc.status_code, msg=exc.detail, data=None)
    return JSONResponse(content=content, status_code=500)


def RequestValidationHandler(_: Request, exc: RequestValidationError) -> JSONResponse:
    content = dict(code=HTTPStatus.UNPROCESSABLE_ENTITY, msg=f"参数错误, {exc}")
    return JSONResponse(content=content, status_code=HTTPStatus.UNPROCESSABLE_ENTITY)


def ResponseValidationHandler(_: Request, exc: ResponseValidationError) -> JSONResponse:
    content = dict(code=HTTPStatus.INTERNAL_SERVER_ERROR, msg=f"处理错误, {exc}")
    return JSONResponse(content=content, status_code=HTTPStatus.INTERNAL_SERVER_ERROR)
