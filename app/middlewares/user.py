from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Update

from app.commands import set_admins_commands, remove_admins_command
from data.config import ADMINS


class UserMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: Dict[str, Any],
    ) -> Any:
        is_admin = False
        global update
        if event.message:
            update = event.message
            is_admin = update.from_user.id in ADMINS and update.chat.type == 'private'
        elif event.callback_query:
            update = event.callback_query
            await update.answer()
            if update.inline_message_id:
                is_admin = False
            else:
                is_admin = update.from_user.id in ADMINS and update.message.chat.type == 'private'
        elif event.inline_query:
            update = event.inline_query
        if update.from_user.id in ADMINS:
            await set_admins_commands(update.from_user.id)
        else:
            await remove_admins_command(update.from_user.id)
        data['is_admin'] = is_admin
        return await handler(event, data)
