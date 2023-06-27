import calendar
from datetime import timedelta

from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from app.keyboards import week_markup
from app.routers import user_router as router
from database.models import Day
from database.services import get_days
from loader import _
from utils import current_time


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
    for day in days:
        if day.subjects:
            text += f'\n\n{calendar.day_name[day.day_id]}'
            for si, subject in enumerate(day.subjects):
                text += f'\n{si + 1}) <b>{subject.subject.name}</b>({subject.subject.audience})'
    return text if text else _('Schedule is empty🫡')


def _get_schedule_data(shift: str = 'this'):
    _current_time = current_time()
    if shift == 'next':
        _current_time += timedelta(weeks=1)

    text = _get_schedule_text(get_days(_current_time.isocalendar().week))
    markup = week_markup('schedule', shift)
    return text, markup
