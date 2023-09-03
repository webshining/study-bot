from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import Update

from database.services import get_or_create_chat, get_or_create_user


class UserMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: Dict[str, Any],
    ) -> Any:
        if event.message:
            message = event.message
            chat_id = message.chat.id
        elif event.callback_query:
            message = event.callback_query
            chat_id = message.message.chat.id
        elif event.inline_query:
            message = event.inline_query
            chat_id = message.from_user.id
        
        data['group_id'] = get_or_create_chat(message.from_user.id).group_id or get_or_create_chat(chat_id).group_id
        data['user'] = get_or_create_user(message.from_user.full_name, message.from_user.id, message.from_user.username)
        return await handler(event, data)
