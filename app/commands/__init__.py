from aiogram.types import BotCommandScopeChat

from loader import bot, i18n

from .default import get_default_commands, set_default_commands
from .admins import get_admins_commands, set_admins_commands
from .super_admins import get_super_admins_commands, set_super_admins_commands


async def remove_admins_commands(id: int):
    await bot.delete_my_commands(scope=BotCommandScopeChat(chat_id=id))
    for lang in i18n.available_locales:
        await bot.delete_my_commands(scope=BotCommandScopeChat(chat_id=id), language_code=lang)
