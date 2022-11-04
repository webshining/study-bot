import calendar, pytz
from datetime import datetime, timedelta
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from loader import dp, bot
from database.models import Day
from database.services import get_days
from app.keyboards import get_week_makrup


@dp.message(Command('schedule'))
async def schedule_handler(message: Message):
    text, markup = _get_schedule_data()
    await message.answer(text=text, reply_markup=markup)
    
    
@dp.callback_query(lambda call: call.data.startswith('schedule'))
async def schedule_callback_handler(call: CallbackQuery):
    await call.answer()
    if call.data[9:] == 'next':
        date = datetime.now(pytz.timezone('Europe/Kiev')) + timedelta(weeks=1)
    else:
        date = datetime.now(pytz.timezone('Europe/Kiev'))
    days = get_days(date.isocalendar().week)
    text = _get_schedule_text(days)
    markup = get_week_makrup('schedule', call.data[9:])
    try:
        if call.inline_message_id:
            await bot.edit_message_text(text, message_id=call.inline_message_id, inline_message_id=call.inline_message_id, reply_markup=markup)
        else:
            await bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=markup)
    except:
        pass
    

def _get_schedule_text(days: list[Day]):
    text = ''
    for index, day in enumerate(days):
        if day.subjects:
            text += f'\n\n{calendar.day_name[index]}'
            for i, subject in enumerate(day.subjects):
                text += f'\n{i+1}) <b>{subject.subject.name}</b>'
                text += f'({subject.subject.audience})' if subject.subject.audience else ''
                text += f'[{subject.group}]' if subject.group else ''
    
    return text if text else 'Schedule is empty🫡'


def _get_schedule_data():
    shift = 'this'
    current_time = datetime.now(pytz.timezone('Europe/Kiev'))
    if current_time.weekday() >= 5:
        current_time += timedelta(weeks=1)
        shift = 'next'
    
    text = _get_schedule_text(get_days(current_time.isocalendar().week))
    markup = get_week_makrup('schedule', shift)
    return text, markup
