from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import Message

from app.commands import remove_admins_command, set_admins_commands
from data.config import ADMINS


class UserMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        if event.from_user.id in ADMINS:
            await set_admins_commands(event.from_user.id)
        else:
            await remove_admins_command(event.from_user.id)
        return await handler(event, data)