from app.routers import user_router

from .user import UserMiddleware


def setup_middlewares():
    user_router.message.middleware(UserMiddleware())