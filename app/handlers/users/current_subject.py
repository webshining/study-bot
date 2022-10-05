from datetime import datetime
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Command

from loader import dp
from database.services import get_day_by_date


@dp.message_handler(Command('current'))
async def current_handler(message: Message):
    current_time = datetime.now()
    time = str(current_time.time())
    day = get_day_by_date(current_time)
    subjects = day.subjects
    subject_now = [s for s in subjects if s.time_start <= time <= s.time_end]
    if time > subjects[-1].time_end:
        text = f'This was the last.'
    if subject_now:
        text = f'Now a couple of <b>{subject_now[0].name}</b>\nTeacher: <b>{subject_now[0].teacher}</b>'
        text += f'\nAudience: <b>{subject_now[0].audience}</b>' if subject_now[0].audience else ''
        text += f'\n\nInfo: <b>{subject_now[0].info}</b>' if subject_now[0].info else ''
    await message.answer(text)
    