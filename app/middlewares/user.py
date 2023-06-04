from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import Update


class UserMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: Dict[str, Any],
    ) -> Any:
        global chatId
        if event.message:
            chatId = event.message.chat.id
        elif event.callback_query:
            update = event.callback_query
            if update.inline_message_id:
                chatId = update.from_user.id
            else:
                chatId = update.message.chat.id
        elif event.inline_query:
            chatId = event.inline_query.from_user.id
        data['chat'] = chatId
        return await handler(event, data)
