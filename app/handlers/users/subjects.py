from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from app.keyboards import get_subjects_keyboard
from loader import dp
from database import get_subjects


@dp.message_handler(Command('subjects'))
async def subjects_handler(message: Message):
    subjects = get_subjects()
    if not subjects:
        return await message.answer('Subjects list is empty!')
    await message.answer('Select subject to check info:', reply_markup=get_subjects_keyboard('subjects', subjects))
