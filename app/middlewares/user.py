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
        global from_user
        if event.message:
            from_user = event.message.from_user
        elif event.callback_query:
            from_user = event.callback_query.from_user
        elif event.inline_query:
            from_user = event.inline_query.from_user
        if from_user.id in ADMINS:
            await set_admins_commands(from_user.id)
        else:
            await remove_admins_command(from_user.id)
        return await handler(event, data)