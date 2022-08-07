from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Command
from database import get_subject, get_subjects
from loader import _, dp
from app.keyboards import get_subjects_markup, get_files_markup


@dp.message_handler(Command('subjects'))
async def info_handler(message: Message):
    await message.answer(_('Select subject:'), reply_markup=get_subjects_markup(get_subjects()))


@dp.callback_query_handler(lambda call: call.data.startswith('subjects'))
async def subject_info_handler(call: CallbackQuery):
    text, markup = _get_subject_text(get_subject(call.data[9:]))
    await call.message.answer(text, reply_markup=markup)


@dp.callback_query_handler(lambda call: call.data.startswith('info'))
async def subject_file_handler(call: CallbackQuery):
    await call.message.answer_document(call.data[5:])


def _get_subject_text(subject):
    markup = None
    text = ''
    text += _('<b>{}</b>\n\nAudience: {}\nTeacher: {}\n\n').format(subject.name, subject.audience, subject.teacher)
    if subject.info:
        text += subject.info
    if subject.files:
        markup = get_files_markup('info', subject.files)
        text += _('\n\nDocument list:')
    return text, markup
