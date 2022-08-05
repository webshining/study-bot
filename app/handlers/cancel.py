from aiogram.dispatcher.filters import Command
from aiogram.types import Message
from loader import dp, _


@dp.message_handler(Command('cancel'), state="*")
async def message_handler(message: Message):
    await message.answer(_('All actions have been reset!'))
