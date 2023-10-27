from aiogram.types import BotCommand, BotCommandScopeChat

from loader import _, bot, i18n

from .admins import get_admins_commands


def get_super_admins_commands(lang: str = 'en'):
    commands = get_admins_commands(lang)
    commands.extend([
        BotCommand(command='/users', description=_('get users list [admin]', locale=lang)),
    ])
    return commands


async def set_super_admins_commands(id: int):
    await bot.set_my_commands(get_super_admins_commands(), scope=BotCommandScopeChat(chat_id=id))
    for lang in i18n.available_locales:
        await bot.set_my_commands(get_super_admins_commands(lang), scope=BotCommandScopeChat(chat_id=id),
                                  language_code=lang)