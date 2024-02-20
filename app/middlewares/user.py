from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import Update

from database.models import User


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
        else:
            message = event.inline_query

        data['user'] = await User.get_or_create(id=message.from_user.id, name=message.from_user.full_name,
                                                username=message.from_user.username)
        return await handler(event, data)
