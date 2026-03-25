from fastapi import APIRouter

from .user_apis import router as user_router
from .role_apis import router as role_router
from .permission_apis import router as permission_router

v1_router = APIRouter(prefix="/v1", tags=["v1"])

v1_router.include_router(user_router)
v1_router.include_router(role_router)
v1_router.include_router(permission_router)
