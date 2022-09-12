from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery
from app.keyboards import get_subjects_markup
from database.models import Subject
from database.services import get_subjects, get_subject
from loader import dp


@dp.message_handler(Command('subjects'))
async def subjects_handler(message: Message):
    subjects = get_subjects()
    if subjects:
        await message.answer('Select subject:', reply_markup=get_subjects_markup('info', subjects))
    else:
        await message.answer('Subjects list empty!')


@dp.callback_query_handler(lambda call: call.data.startswith('info'))
async def subjects_info_handler(call: CallbackQuery):
    subject = get_subject(call.data[5:])
    text = _get_subject_text(subject)
    await call.message.answer(text)
    await call.answer()


def _get_subject_text(subject: Subject):
    text = f'<b>{subject.name}:</b>\nAudience: <b>{subject.audience}</b>\nTeacher: <b>{subject.teacher}</b>'
    if subject.info:
        text += f'\n\n{subject.info}'

    return text
