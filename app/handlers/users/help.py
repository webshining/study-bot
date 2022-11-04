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
                      '\nCreator: <b>@webshining</b>😉'))
    await message.answer(text)
