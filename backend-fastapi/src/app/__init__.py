from contextlib import asynccontextmanager

from fastapi import FastAPI
from tortoise import Tortoise

from app.config import settings
from app.core.app_init import init_data, add_middlewares, add_exception_handlers, add_routers


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_data()
    yield
    await Tortoise.close_connections()


def create_app() -> FastAPI:
    app = FastAPI(
        debug=settings.app.debug,
        title=settings.app.title,
        description=settings.app.description,
        version=settings.app.version,
        lifespan=lifespan,
    )

    # Middlewares
    add_middlewares(app)
    # Exception handlers
    add_exception_handlers(app)
    # Routers
    add_routers(app)
    return app


app = create_app()
