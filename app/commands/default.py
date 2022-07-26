from aiogram.types import BotCommand, BotCommandScopeDefault

from loader import bot


def get_default_commands():
    commands = [
        BotCommand(command='/start', description='start message'),
        BotCommand(command='/schedule', description='schedule'),
        BotCommand(command='/subjects', description='subjects info'),
        BotCommand(command='/current', description='current subject'),
        BotCommand(command='/lists', description='get lists'),
        BotCommand(command='/lists_set', description='add an entry to the list'),
        BotCommand(command='/cancel', description='reset state'),
        BotCommand(command='/help', description='how is works'),
    ]
    return commands


async def set_default_commands():
    await bot.set_my_commands(get_default_commands(), scope=BotCommandScopeDefault())
    