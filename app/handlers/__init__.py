from aiogram import Dispatcher

from . import cancel
from .admins import router as admin_router
from .users import router as user_router


def setup_handlers(dp: Dispatcher):
    dp.include_routers(user_router, admin_router)
