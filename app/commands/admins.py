from aiogram.types import BotCommand, BotCommandScopeChat

from loader import bot
from .default import get_default_commands


def get_admins_commands():
    commands = get_default_commands()
    commands.extend([
        BotCommand(command='/create_list', description='create new list'),
        BotCommand(command='/edit_list', description='edit an existing list'),
        BotCommand(command='/delete_list', description='delete list'),
    ])
    return commands


async def set_admins_commands(id: int):
    await bot.set_my_commands(get_admins_commands(), scope=BotCommandScopeChat(chat_id=id))
    