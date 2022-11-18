from aiogram.types import Message
from aiogram.filters import Command
from loader import dp


@dp.message(Command('help'))
async def help_handler(message: Message):
    text = '\n'.join((f'Hello <b>{message.from_user.full_name}</b>👋',
                      f'I am a diary bot',
                      f'\nCommands:',
                      '/help - All infos',
                      '/subjects - Get subjects info',
                      '/schedule - Get schedule',
                      '/current - Get current info',
                      '/lists - Get lists'
                      '/lists_set - Add an entry to the list (if you have already added data to the list, they will be changed and not added again)'
                      '\n\nCreator: <b>@webshining</b>😉',
                      'Repositofy: <b><a href="https://gitfront.io/r/user-1330244/DkqZMaFsoi7n/study-bot/">GitHub</a></b>'))
    await message.answer(text, disable_web_page_preview=True)
