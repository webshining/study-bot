from aiogram import Dispatcher

from app.routers import user_router


def setup_middleware(dp: Dispatcher):
    from .inter import i18n_middleware
    from .user import UserMiddleware
    user_router.message.middleware(UserMiddleware())
    user_router.message.middleware(i18n_middleware)
    dp.update.middleware(i18n_middleware)
    