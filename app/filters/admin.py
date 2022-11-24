from aiogram.types import Update
from aiogram.filters import BaseFilter

from data.config import ADMINS


class AdminFilter(BaseFilter):
    async def __call__(self, update: Update) -> bool:
        if update.message:
            from_user = update.message.from_user
        elif update.callback_query:
            from_user = update.callback_query.from_user
        elif update.inline_query:
            from_user = update.inline_query.from_user
        return from_user.id in ADMINS
