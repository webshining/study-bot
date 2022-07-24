from aiogram.types import BotCommand, BotCommandScopeDefault
from loader import i18n, _


def get_default_commands(lang: str = 'en') -> list[BotCommand]:
    commands = [
        BotCommand('/start', _('start bot', locale=lang)),
        BotCommand('/help', _('how it works?', locale=lang)),
        BotCommand('/lang', _('change language', locale=lang)),
    ]

    return commands


async def set_default_commands(bot):
    await bot.set_my_commands(get_default_commands(), scope=BotCommandScopeDefault())
    for lang in i18n.available_locales:
        await bot.set_my_commands(get_default_commands(lang), scope=BotCommandScopeDefault(), language_code=lang)
