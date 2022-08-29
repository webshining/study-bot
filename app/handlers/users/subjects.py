from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Command
from app.keyboards import get_subjects_markup
from loader import dp
from database import get_subjects, get_subject


@dp.message_handler(Command('subjects'), status='admin')
async def subjects_handler(message: Message):
    if not await get_subjects():
        return await message.answer('Subjects list is empty!')
    await message.answer('Select subject:', reply_markup=get_subjects_markup('info', await get_subjects()))


@dp.callback_query_handler(lambda call: call.data.startswith('info'))
async def subject_handler(call: CallbackQuery):
    subject = await get_subject(call.data[5:])
    text = f'<b>{subject.name}</b>:\nAudience: <b>{subject.audience}</b>\nTeacher: <b>{subject.teacher}</b>\n\n {subject.info if subject.info != "" else ""}'
    await call.message.answer(text)
