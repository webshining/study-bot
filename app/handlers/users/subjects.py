from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Command

from loader import dp, bot
from database.models import Subject
from database.services import get_subjects, get_subject
from app.keyboards import get_subjects_makrup, get_back_markup


@dp.message_handler(Command('subjects'))
async def subjects_handler(message: Message):
    text, markup = _get_subjects_data()
    await message.answer(text, reply_markup=markup)
    

@dp.callback_query_handler(lambda call: call.data.startswith('info'))
async def subjects_callback_handler(call: CallbackQuery):
    await call.answer()
    if call.data[5:] == 'back':
        subjects = get_subjects()
        if not subjects:
            return await call.message.edit_text('Subjects is empty🫡')
        markup = get_subjects_makrup('info', subjects)
        if call.inline_message_id:
            return await bot.edit_message_text('Select subject📚:', message_id=call.inline_message_id, inline_message_id=call.inline_message_id, reply_markup=markup)
        return await call.message.edit_text('Select subject📚:', reply_markup=markup)
    if call.inline_message_id:
        return await bot.edit_message_text(_get_subject_text(get_subject(call.data[5:])), message_id=call.inline_message_id, inline_message_id=call.inline_message_id, reply_markup=get_back_markup('info'))
    await call.message.edit_text(text=_get_subject_text(get_subject(call.data[5:])), reply_markup=get_back_markup('info'))


def _get_subject_text(subject: Subject):
    text = f'<b><i>{subject.name}:</i></b>\nTeacher: <b>{subject.teacher}</b>'
    if subject.audience:
        text += f'\nAudience: <b>{subject.audience}</b>'
    if subject.info:
        text += f'\n\n{subject.info}'
    
    return text


def _get_subjects_data():
    subjects = get_subjects()
    markup = get_subjects_makrup('info', subjects)
    text = 'Select subject📚:' if subjects else "Subjects is empty🫡"
    return text, markup