from aiogram.types import Message
from aiogram.dispatcher.filters import BoundFilter
from database import get_user


class StatusFilter(BoundFilter):
    key = 'status'

    def __init__(self, status: str):
        self.status = status

    async def check(self, message: Message):
        user = await get_user(message.from_user.id)

        return user.status == self.status if user else False
