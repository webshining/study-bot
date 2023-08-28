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
        user = get_or_create_user(event.from_user.full_name, event.from_user.id, event.chat.id)
        if user.status not in ('admin', 'super_admin'):
            await remove_admins_command(user.user_id)
            return await event.answer(_("Not enough rights🚫"))
        await set_admins_commands(user.user_id)
        data['user'] = user
        return await handler(event, data)
