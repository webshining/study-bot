from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import Update

from database.services import get_or_create_user


class UserMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
            event: Update,
            data: Dict[str, Any],
    ) -> Any:
        if event.message:
            message = event.message
        elif event.callback_query:
            message = event.callback_query
        elif event.inline_query:
            message = event.inline_query

        data['user'] = get_or_create_user(user_id=message.from_user.id, name=message.from_user.full_name,
                                          username=message.from_user.username)
        return await handler(event, data)
