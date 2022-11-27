from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from loader import dp, bot, _
from database.models import Subject
from database.services import get_subjects, get_subject
from app.keyboards import get_subjects_markup


@dp.message(Command('subjects'))
async def subjects_handler(message: Message):
    text, markup = _get_subjects_data()
    await message.answer(text, reply_markup=markup)


@dp.callback_query(lambda call: call.data.startswith('subject'))
async def subjects_callback_handler(call: CallbackQuery):
    await call.answer()
    subject = get_subject(call.data[9:])
    text, markup = _get_subject_data(subject)
    if call.inline_message_id:
        await bot.edit_message_text(text=text, reply_markup=markup, inline_message_id=call.inline_message_id)
    else:
        await call.message.edit_text(text, reply_markup=markup)


def _get_subject_text(subject: Subject):
    text = _('Subject not found🫡')
    if subject:
        text = _('<b>{}:</b>\nTeacher: <b>{}</b>').format(subject.name, subject.teacher)
        if subject.audience:
            text += _('\nAudience: <b>{}</b>').format(subject.audience)
        if subject.info:
            text += f'\n\n{subject.info}'

    return text


def _get_subject_data(subject: Subject):
    text = _get_subject_text(subject)
    markup = None
    return text, markup


def _get_subjects_data():
    subjects = get_subjects()
    markup = get_subjects_markup('subject', subjects)
    text = _('Select subject📚:') if subjects else _("Subjects is empty🫡")
    return text, markup.as_markup()
