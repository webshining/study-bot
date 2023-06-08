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
        global chat_id
        if event.message:
            id = event.message.from_user.id
            chat_id = event.message.chat.id
            name = event.message.from_user.full_name
        elif event.callback_query:
            id = event.callback_query.from_user.id
            update = event.callback_query
            if update.inline_message_id:
                chat_id = update.from_user.id
            else:
                chat_id = update.message.chat.id
            name = event.callback_query.from_user.full_name
        elif event.inline_query:
            id = event.inline_query.from_user.id
            chat_id = event.inline_query.from_user.id
            name = event.inline_query.from_user.full_name
        user = get_or_create_user(name=name, user_id=id, chat_id=chat_id)
        data['user'] = user
        return await handler(event, data)
