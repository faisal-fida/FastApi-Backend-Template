from fastapi.routing import APIRouter

from reworkd_platform.web.api import auth, models

api_router = APIRouter()
api_router.include_router(models.router, prefix="/models", tags=["models"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
