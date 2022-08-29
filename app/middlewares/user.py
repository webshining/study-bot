from aiogram.types import Message
from aiogram.dispatcher.middlewares import BaseMiddleware

from database import get_or_create_user


class UserMiddleware(BaseMiddleware):
    @staticmethod
    async def on_process_message(message: Message, data):
        from_user = message.from_user
        data['users'] = await get_or_create_user(from_user.id, from_user.full_name, from_user.username)
