from aiogram import Dispatcher

from app.routers import admin_router, user_router

from .admins import users
from .users import (call_schedule, current_lesson, inline, schedule,
                    select_group, start)


def setup_handlers(dp: Dispatcher):
    dp.include_routers(user_router, admin_router)