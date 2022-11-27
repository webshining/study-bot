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
        if event.message:
            update = event.message
        elif event.callback_query:
            update = event.callback_query
            await update.answer()
        elif event.inline_query:
            update = event.inline_query.chat_type
        if update.from_user.id in ADMINS:
            await set_admins_commands(update.from_user.id)
        else:
            await remove_admins_command(update.from_user.id)
        data['is_admin'] = update.from_user.id in ADMINS
        return await handler(event, data)
