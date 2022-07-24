from aiogram.types import Message
from aiogram.dispatcher.filters import CommandStart
from loader import dp, _


@dp.message_handler(CommandStart())
async def start_handler(message: Message):
    text = _('Hello <b>{}</b>', locale='ru')
    await message.answer(text.format(message.from_user.full_name))
