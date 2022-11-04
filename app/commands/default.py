from aiogram.types import BotCommand, BotCommandScopeDefault

from loader import bot


def get_default_commands():
    commands = [
        BotCommand(command='/start', description='Start message'),
        BotCommand(command='/schedule', description='schedule'),
        BotCommand(command='subjects', description='subjects info'),
        BotCommand(command='current', description='current subject')
    ]
    return commands


async def set_default_commands():
    await bot.set_my_commands(get_default_commands(), scope=BotCommandScopeDefault())
    