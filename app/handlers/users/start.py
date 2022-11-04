from aiogram.types import Message
from aiogram.filters import Command
from loader import dp


@dp.message(Command('start'))
async def start_handler(message: Message):
    text = '\n'.join((f'Hello <b>{message.from_user.full_name}</b>👋',
                      f'Write /help to see more information'))
    await message.answer(text)
