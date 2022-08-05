from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message
from database import get_or_create_user


class UserMiddleware(BaseMiddleware):
    @staticmethod
    async def on_process_message(message: Message, data: dict):
        from_user = message.from_user
        data['user'] = get_or_create_user(from_user.id, from_user.full_name, from_user.username)
