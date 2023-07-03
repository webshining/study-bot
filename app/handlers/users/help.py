from aiogram.filters import Command
from aiogram.types import Message

from app.commands import get_admins_commands, get_default_commands
from app.routers import user_router as router


@router.message(Command('help'))
async def help_handler(message: Message, user):
    text = '\n'.join((f'Hello <b>{message.from_user.full_name}</b>👋',
                      f'I am a diary bot',
                      f'<b>\nCommands:</b>'))
    commands = get_admins_commands() if user.status == 'admin' and message.chat.type == 'private' else get_default_commands()
    for command in commands:
        text += f'\n{command.command} - {command.description}'

    text += '\n'.join(('\n\nCreator: <b>@webshining</b>😉',
                       'Repositofy: <b><a href="https://github.com/webshining/study-bot">GitHub</a></b>'))
    await message.answer(text, disable_web_page_preview=True)
