from aiogram import Dispatcher

from app.routers import admin_router

from .admin import AdminMiddleware
from .inter import i18n_middleware
from .user import UserMiddleware


def setup_middleware(dp: Dispatcher):
    dp.update.middleware(UserMiddleware())
    dp.update.middleware(i18n_middleware)
    admin_router.message.middleware(AdminMiddleware())
