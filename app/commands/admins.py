from aiogram.types import BotCommand, BotCommandScopeChat

from loader import bot
from .default import get_default_commands


def get_admins_commands():
    commands = get_default_commands()
    commands.extend([
        BotCommand(command='/lists_create', description='create list'),
        BotCommand(command='/lists_edit', description='edit list'),
        BotCommand(command='/lists_delete', description='delete list'),
    ])
    return commands


async def set_admins_commands(id: int):
    await bot.set_my_commands(get_admins_commands(), scope=BotCommandScopeChat(chat_id=id))


async def remove_admins_command(id: int):
    await bot.set_my_commands(get_default_commands(), scope=BotCommandScopeChat(id))
    