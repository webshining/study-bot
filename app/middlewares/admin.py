from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import Message

from app.commands import set_admins_commands, remove_admins_commands
from database.services import get_or_create_user
from loader import _


class AdminMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any],
    ) -> Any:
        user = get_or_create_user(user_id=event.from_user.id, name=event.from_user.full_name,
                                  username=event.from_user.username)
        if user.status in ('admin', 'super_admin') and event.chat.type != 'private':
            await set_admins_commands(user.user_id)
        else:
            await remove_admins_commands(user.user_id)
            return await event.answer(_("Not enough rights🚫"))
        return await handler(event, data)
