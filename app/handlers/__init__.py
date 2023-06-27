from aiogram import Dispatcher

from app.routers import admin_router, user_router

from . import cancel
from .users import current, help, inline_mode, schedule, start, subjects


def setup_handlers(dp: Dispatcher):
    dp.include_routers(user_router, admin_router)