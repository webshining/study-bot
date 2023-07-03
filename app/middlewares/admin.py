from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import Message

from database.services import get_or_create_user


class AdminMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        user = get_or_create_user(user_id=event.from_user.id, name=event.from_user.full_name, username=event.from_user.username)
        if user.status != 'admin':
            return await event.answer("Not enough rights🚫")
        data['user'] = user
        return await handler(event, data)
        