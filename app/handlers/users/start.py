from aiogram.types import Message
from aiogram.dispatcher.filters import Command
from loader import dp


@dp.message_handler(Command('start'))
async def start_handler(message: Message):
    text = '\n'.join((f'Hello <b>{message.from_user.full_name}</b>👋',
                      f'Write /help to see more information',
                      f'Sorry for the very low speed of the bot, the database servers are free as are the bot servers, so at night the bot will work slower than usual, during the day everything will be fine'))
    await message.answer(text)
