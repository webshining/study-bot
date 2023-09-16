from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from app.keyboards import get_subjects_markup
from app.routers import user_router as router
from database.services import get_subject, get_subjects
from loader import _, bot


@router.message(Command('subjects'))
async def subjects_handler(message: Message):
    text, markup = _get_subjects_data()
    await message.answer(text, reply_markup=markup)


@router.callback_query(lambda call: call.data.startswith('subject'))
async def subjects_callback_handler(call: CallbackQuery):
    text, markup = _get_subject_data(call.data[9:])
    if call.inline_message_id:
        return await bot.edit_message_text(text=text, reply_markup=markup, inline_message_id=call.inline_message_id)
    await call.message.edit_text(text, reply_markup=markup)
    await call.answer()


def _get_subject_data(id: str):
    subject = get_subject(id)
    if not subject:
        return _('Subject not found🫡'), None
    text = _('<b>{}:</b>\nTeacher: <b>{}</b>\nAudience: <b>{}</b>').format(subject.name, subject.teacher,
                                                                           subject.audience)
    if subject.info:
        text += f'\n\n{subject.info}'
    return text, None


def _get_subjects_data():
    subjects = get_subjects()
    markup = get_subjects_markup('subject', subjects)
    text = _('Select subject📚:') if subjects else _("Subjects is empty🫡")
    return text, markup
