from aiogram import Dispatcher

from app.routers import admin_router, user_router

from . import cancel
from .admins import call_all, users
from .users import call_schedule, current_lesson, help, inline, schedule, start


def setup_handlers(dp: Dispatcher):
    dp.include_routers(user_router, admin_router)