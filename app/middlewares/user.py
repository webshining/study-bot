from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Update

from database.services import get_chat
from data.config import ADMINS

class UserMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: Dict[str, Any],
    ) -> Any:
        is_admin = False
        global chatId
        if event.message:
            update = event.message
            chatId = update.chat.id
            is_admin = update.from_user.id in ADMINS
        elif event.callback_query:
            update = event.callback_query
            if update.inline_message_id:
                chatId = update.from_user.id
            else:
                chatId = update.message.chat.id
                is_admin = update.from_user.id in ADMINS
        elif event.inline_query:
            update = event.inline_query
            chatId = update.from_user.id
        data['is_admin'] = is_admin
        data['chat'] = get_chat(chatId)
        return await handler(event, data)
