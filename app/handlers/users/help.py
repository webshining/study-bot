from aiogram.types import Message
from aiogram.filters import Command

from loader import dp, _
from app.commands import get_default_commands, get_admins_commands


@dp.message(Command('help'))
async def help_handler(message: Message, is_admin: bool):
    text = _('Hello <b>{}</b>👋\nI am a diary bot\n<b>\nCommands:</b>').format(message.from_user.full_name)
    for command in get_admins_commands(message.from_user.language_code) if is_admin else get_default_commands(message.from_user.language_code):
        text += f'\n{command.command} - {command.description.capitalize()}'

    text += _('\n\nCreator: <b>@webshining</b>😉\nRepositofy: <b><a href="https://github.com/webshining/study-bot">GitHub</a></b>')
    await message.answer(text, disable_web_page_preview=True)
