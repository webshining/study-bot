from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery
from loader import dp, _, bot
from database import get_subjects, get_subject
from app.keyboards import get_subjects_keyboard


@dp.message_handler(Command('subjects'))
async def subjects_handler(message: Message):
    if not get_subjects():
        return await message.answer('Subject list is empty')
    await message.answer('Select subject:', reply_markup=get_subjects_keyboard(get_subjects()))


@dp.callback_query_handler()
async def subject_handler(call: CallbackQuery):
    text = _get_subject_text(get_subject(int(call.data[-1])), call.from_user.language_code)
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text,
                                reply_markup=None)


def _get_subject_text(subject, lang: str):
    text = ''
    text += _('<b>{}</b>\n\n'
              'Audience: <b>{}</b>\n'
              'Teacher: <b>{}</b>\n\n'
              '{}', locale=lang).format(subject.name, subject.audience, subject.teacher, subject.info)
    if subject.files:
        text += '\n\bFiles:'
    return text
