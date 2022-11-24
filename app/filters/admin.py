from aiogram.types import Update
from aiogram.filters import BaseFilter

from data.config import ADMINS


class AdminFilter(BaseFilter):
    async def __call__(self, update: Update) -> bool:
        return update.from_user.id in ADMINS
