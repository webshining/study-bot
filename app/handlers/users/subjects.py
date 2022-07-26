from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from loader import dp, bot
from database.models import Subject
from database.services import get_subjects, get_subject
from app.keyboards import get_subjects_makrup


@dp.message(Command('subjects'))
async def subjects_handler(message: Message):
    text, markup = _get_subjects_data()
    await message.answer(text, reply_markup=markup)


@dp.callback_query(lambda call: call.data.startswith('subjects'))
async def subjects_callback_handler(call: CallbackQuery):
    await call.answer()
    subject = get_subject(call.data[9:])
    text, markup = _get_subject_data(subject)
    if call.inline_message_id:
        await bot.edit_message_text(text=text, reply_markup=markup, inline_message_id=call.inline_message_id)
    else:
        await call.message.edit_text(text, reply_markup=markup)


def _get_subject_text(subject: Subject):
    text = f'<b><i>{subject.name}:</i></b>\nTeacher: <b>{subject.teacher}</b>'
    if subject.audience:
        text += f'\nAudience: <b>{subject.audience}</b>'
    if subject.info:
        text += f'\n\n{subject.info}'

    return text


def _get_subject_data(subject: Subject):
    text = _get_subject_text(subject)
    markup = None
    return text, markup


def _get_subjects_data():
    subjects = get_subjects()
    markup = get_subjects_makrup('subjects', subjects)
    text = 'Select subject📚:' if subjects else "Subjects is empty🫡"
    return text, markup
