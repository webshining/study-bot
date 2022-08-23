from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery
from app.keyboards import get_subjects_keyboard
from database import get_subjects
from database.services.subjects import get_subject
from loader import dp


@dp.message_handler(Command('subjects'))
async def subjects_handler(message: Message):
    await message.answer('Select subject:', reply_markup=get_subjects_keyboard('subjects', get_subjects()))
    
    

@dp.callback_query_handler(lambda call: call.data.startswith('subjects'))
async def subject_handler(call: CallbackQuery):
    await call.message.answer(_get_subject_text(get_subject(call.data[9:])))
    
    

def _get_subject_text(subject):
    text = ''
    text += f'<b>{subject.name}</b>\nAudience: <b>{subject.audience}</b>\nTeacher: <b>{subject.teacher}</b>'
    if subject.info:
        text += f'\n\n{subject.info}'
    
    return text
