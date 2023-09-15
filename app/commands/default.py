from aiogram.types import BotCommand, BotCommandScopeDefault

from loader import _, bot, i18n


def get_default_commands(lang: str = 'en'):
    commands = [
        BotCommand(command='/start', description=_('start message', locale=lang)),
        BotCommand(command='/current_lesson', description=_('get current lesson', locale=lang)),
        BotCommand(command='/schedule', description=_('get schedule', locale=lang)),
        BotCommand(command='/call_schedule', description=_('get call schedule', locale=lang)),
        # BotCommand(command='/tasks', description=_('get tasks', locale=lang)),
        # BotCommand(command='/edit_task', description=_('edit task', locale=lang)),
        # BotCommand(command='/create_task', description=_('create task', locale=lang)),
        BotCommand(command='/select_group', description=_('select your group', locale=lang)),
    ]
    return commands


async def set_default_commands():
    await bot.set_my_commands(get_default_commands(), scope=BotCommandScopeDefault())
    for lang in i18n.available_locales:
        await bot.set_my_commands(get_default_commands(lang), scope=BotCommandScopeDefault(), language_code=lang)
