from aiogram import Dispatcher

from app.routers import admin_router, user_router


def setup_middleware(dp: Dispatcher):
    from .admin import AdminMiddleware
    from .inter import i18n_middleware
    from .user import UserMiddleware
    user_router.message.middleware(UserMiddleware())
    user_router.message.middleware(i18n_middleware)
    admin_router.message.middleware(AdminMiddleware())
    dp.update.middleware(i18n_middleware)
    