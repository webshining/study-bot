from app.routers import admin_router, user_router

from .admin import AdminMiddleware
from .user import UserMiddleware


def setup_middlewares():
    admin_router.message.middleware(AdminMiddleware())
    user_router.message.middleware(UserMiddleware())