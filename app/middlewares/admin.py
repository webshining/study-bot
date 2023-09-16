from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import Message

from app.commands import remove_admins_commands, set_admins_commands, set_super_admins_commands
from database.services import get_or_create_user
from loader import _


class AdminMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any],
    ) -> Any:
        user = get_or_create_user(event.from_user.full_name, event.from_user.id, event.from_user.username)
        if user.status == 'super_admin':
            await set_super_admins_commands(user.user_id)
        elif user.status == 'admin':
            await set_admins_commands(user.user_id)
        else:
            await remove_admins_commands(user.user_id)
            return await event.answer(_("Not enough rights🚫"))
        data['user'] = user
        data['is_super_admin'] = user.status == 'super_admin'
        return await handler(event, data)
