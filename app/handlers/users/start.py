from aiogram.types import Message
from aiogram.filters import Command

from loader import dp, _


@dp.message(Command('start'))
async def start_handler(message: Message):
    text = _('Hello <b>{}</b>👋\nWrite /help to see more information').format(message.from_user.full_name)
    await message.answer(text)
