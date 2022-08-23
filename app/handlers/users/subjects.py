from aiogram.dispatcher.filters import Command
from aiogram.types import Message
from app.keyboards import get_subjects_keyboard
from database import get_subjects
from loader import dp


@dp.message_handler(Command('subjects'))
async def subjects_handler(message: Message):
    await message.answer('Select subject:', reply_markup=get_subjects_keyboard('subjects', get_subjects()))
