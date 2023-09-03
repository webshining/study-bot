from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import Update

from app.commands import remove_admins_command, set_admins_commands
from database.services import get_or_create_user
from loader import _


class AdminMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: Dict[str, Any],
    ) -> Any:
        if event.message:
            message = event.message
        elif event.callback_query:
            message = event.callback_query
        elif event.inline_query:
            message = event.inline_query
        user = get_or_create_user(message.from_user.full_name, message.from_user.id, message.from_user.username)
        if user.status not in ('admin', 'super_admin'):
            await remove_admins_command(user.user_id)
            return await event.answer(_("Not enough rights🚫"))
        await set_admins_commands(user.user_id)
        data['user'] = user
        return await handler(event, data)
