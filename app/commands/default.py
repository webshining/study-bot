from aiogram.types import BotCommand, BotCommandScopeDefault, BotCommandScopeChat
from loader import i18n, _, bot


def get_default_commands(lang: str = 'en'):
    commands = [
        BotCommand('/start', _('start chat', locale=lang)),
        BotCommand('/help', _('help with control', locale=lang)),
        BotCommand('/schedule', _('see schedule', locale=lang)),
        BotCommand('/homework', _('see homework', locale=lang)),
        BotCommand('/subjects', _('get subjects info', locale=lang))
    ]
    return commands


async def set_default_commands():
    await bot.set_my_commands(get_default_commands(), scope=BotCommandScopeDefault())
    for lang in i18n.available_locales:
        await bot.set_my_commands(get_default_commands(lang), language_code=lang, scope=BotCommandScopeDefault())


async def set_user_commands(user_id: int, lang: str):
    await bot.set_my_commands(get_default_commands(lang), scope=BotCommandScopeChat(user_id))
