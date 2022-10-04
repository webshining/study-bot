import calendar
from datetime import datetime, timedelta
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Command

from loader import dp
from database.models import Day
from database.services import get_days
from app.keyboards import get_week_makrup


@dp.message_handler(Command('schedule'))
async def schedule_handler(message: Message):
    text, markup = _get_schedule_data()
    await message.answer(text=text, reply_markup=markup)
    
    
@dp.callback_query_handler(lambda call: call.data.startswith('schedule'))
async def schedul_callback_handler(call: CallbackQuery):
    await call.answer()
    if call.data[9:] == 'next':
        date = datetime.now() + timedelta(weeks=1)
    else:
        date = datetime.now()
    
    days = get_days(date.isocalendar().week)
    text = _get_schedule_text(days)
    try:
        await call.message.edit_text(text=text, reply_markup=get_week_makrup('schedule', call.data[9:]))
    except:
        pass
    

def _get_schedule_text(days: list[Day]):
    text = ''
    for index, day in enumerate(days):
        if day.subjects:
            text += f'\n\n{calendar.day_name[index]}'
            for i, subject in enumerate(day.subjects):
                text += f'\n{i+1}) <b>{subject.name}</b>'
                text += f'({subject.audience})' if subject.audience else ''
    
    return text if text else 'Schedule is empty'


def _get_schedule_data():
    shift = 'this'
    current_time = datetime.now()
    date = current_time
    if current_time.weekday() > 5:
        date += timedelta(weeks=1)
        shift = 'next'
    
    text = _get_schedule_text(get_days(date.isocalendar().week))
    markup = get_week_makrup('schedule', shift)
    return text, markup
