import calendar
from datetime import timedelta

from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from app.keyboards import get_week_makrup
from app.routers import user_router as router
from database.models import Day
from database.services import get_days
from utils.time import get_current_time


@router.message(Command('schedule'))
async def schedule_handler(message: Message):
    text, markup = _get_schedule_data()
    await message.answer(text=text, reply_markup=markup)


@router.callback_query(lambda call: call.data.startswith('schedule'))
async def schedule_callback_handler(call: CallbackQuery):
    await call.answer()
    text, markup = _get_schedule_data(call.data[9:])
    try:
        if call.inline_message_id:
            await call.message.edit_text(text=text, inline_message_id=call.inline_message_id, reply_markup=markup)
        else:
            await call.message.edit_text(text=text, reply_markup=markup)
    except:
        pass

def _get_schedule_text(days: list[Day]):
    text = ''
    for index, day in enumerate(days):
        if day.subjects:
            text += f'\n\n{calendar.day_name[index]}'
            for i, subject in enumerate(day.subjects):
                text += f'\n{i + 1}) <b>{subject.subject.name}</b>'
                text += f'({subject.subject.audience})' if subject.subject.audience else ''
                text += f'[{subject.group}]' if subject.group else ''

    return text if text else 'Schedule is empty🫡'

def _get_schedule_data(shift: str = 'this'):
    current_time = get_current_time()
    if shift == 'next':
        current_time += timedelta(weeks=1)

    text = _get_schedule_text(get_days(current_time.isocalendar().week))
    markup = get_week_makrup('schedule', shift)
    return text, markup
