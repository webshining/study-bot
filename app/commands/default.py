from aiogram.types import BotCommand, BotCommandScopeDefault

from loader import _, bot, i18n


def get_default_commands(lang: str = 'en'):
    commands = [
        BotCommand(command='/start', description=_('start message', locale=lang)),
        BotCommand(command='/schedule', description=_('get schedule', locale=lang)),
        BotCommand(command='/subjects', description=_('get subjects info', locale=lang)),
        BotCommand(command='/current', description=_('current lesson', locale=lang)),
        BotCommand(command='/cancel', description=_('reset state', locale=lang)),
        BotCommand(command='/help', description=_('how is works', locale=lang)),
    ]
    return commands


async def set_default_commands():
    await bot.set_my_commands(get_default_commands(), scope=BotCommandScopeDefault())
    for lang in i18n.available_locales:
        await bot.set_my_commands(get_default_commands(lang), scope=BotCommandScopeDefault(), language_code=lang)
    