from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import Message

from app.commands import remove_admins_command, set_admins_commands
from database.services import get_or_create_user
from loader import _


class AdminMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        user = get_or_create_user(id=event.from_user.id, name=event.from_user.full_name, username=event.from_user.username)
        if user.status not in ('admin', 'super_admin'):
            await remove_admins_command(user.id)
            return await event.answer(_("Not enough rights🚫"))
        await set_admins_commands(user.id)
        data['user'] = user
        return await handler(event, data)
