from aiogram.types import Message
from aiogram.filters import BaseFilter

from data.config import ADMINS


class AdminFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        from_user = message.from_user
        return from_user.id in ADMINS
