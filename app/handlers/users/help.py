from aiogram.types import Message
from aiogram.dispatcher.filters import Command
from loader import dp


@dp.message_handler(Command('help'))
async def help_handler(message: Message):
    text = '\n'.join((f'Hello <b>{message.from_user.full_name}</b>👋',
                      f'I am a diary bot',
                      f'\nCommands:',
                      '/help - All infos',
                      '/subjects - Get subjects info',
                      '/schedule - Get schedule',
                      '/current - Get current info',
                      '\nCreator: <b>@webshining</b>😉',
                      'Sorry for the very low speed of the bot, the database servers are free as are the bot servers, so at night the bot will work slower than usual, during the day everything will be fine'))
    await message.answer(text)
