from aiogram.filters import Command
from aiogram.types import Message

from app.routers import user_router as router
from data.config import ADMINS


@router.message(Command('help'))
async def help_handler(message: Message):
    text = '\n'.join((f'Hello <b>{message.from_user.full_name}</b>👋',
                      f'I am a diary bot',
                      f'<b>\nCommands:</b>',
                      '/help - All infos',
                      '/subjects - Get subjects info',
                      '/schedule - Get schedule',
                      '/current - Get current info',
                      '/cancel - Reset your state'))
    if message.from_user.id in ADMINS and message.chat.type == 'private':
        text += '\n'.join((f'\n\n👑 Congratulations you are on the list of the best administrators',
                           '<b>Commands:</b>',
                           '➕ /lists_create - Create new list',
                           '✏️ /lists_edit - Edit list name',
                           '❌ /lists_delete - Delete one list'))

    text += '\n'.join(('\n\nCreator: <b>@webshining</b>😉',
                       'Repositofy: <b><a href="https://github.com/webshining/study-bot">GitHub</a></b>'))
    await message.answer(text, disable_web_page_preview=True)
