from datetime import datetime
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Command

from loader import dp
from database.services import get_day_by_date
from app.keyboards import get_update_makrup


@dp.message_handler(Command('current'))
async def current_handler(message: Message):
    text = _get_current_text()
    await message.answer(text, reply_markup=get_update_makrup('current'))


@dp.callback_query_handler(lambda call: call.data.startswith('current'))
async def current_callback_handler(call: CallbackQuery):
    await call.answer()
    text = _get_current_text()
    try:
        await call.message.edit_text(text, reply_markup=get_update_makrup('current'))
    except:
        pass


def _get_current_text():
    current_time = datetime.now()
    time = str(current_time.time())
    day = get_day_by_date(current_time)
    subjects = day.subjects
    subject_now = [s for s in subjects if s.time_start <= time <= s.time_end]
    if time > subjects[-1].time_end:
        text = f'This was the last.'
    if subject_now:
        text = f'Now class of <b>{subject_now[0].name}</b>\nTeacher: <b>{subject_now[0].teacher}</b>'
        text += f'\nAudience: <b>{subject_now[0].audience}</b>' if subject_now[0].audience else ''
        text += f'\n\nInfo: <b>{subject_now[0].info}</b>' if subject_now[0].info else ''
    else:
        text = f'Break now!'
    
    return text