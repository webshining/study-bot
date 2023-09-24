import calendar
from datetime import timedelta

from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from app.keyboards import get_week_markup
from app.routers import user_router as router
from database.models import Day
from database.services import get_days
from loader import _
from utils import get_current_time


@router.message(Command('schedule'))
async def schedule_handler(message: Message):
    text, markup = _get_schedule_data()
    await message.answer(text=text, reply_markup=markup)


@router.callback_query(lambda call: call.data.startswith('schedule'))
async def schedule_callback_handler(call: CallbackQuery):
    text, markup = _get_schedule_data(call.data[9:])
    try:
        if call.inline_message_id:
            await call.message.edit_text(text=text, inline_message_id=call.inline_message_id, reply_markup=markup)
        else:
            await call.message.edit_text(text=text, reply_markup=markup)
    except:
        pass
    await call.answer()


def _get_schedule_data(shift: str = 'this'):
    _current_time = get_current_time()
    if shift == 'next':
        _current_time += timedelta(weeks=1)
    days = get_days(_current_time.isocalendar().week)
    text = _get_schedule_text(days)
    markup = get_week_markup('schedule', shift)
    return text, markup


def _get_schedule_text(days: list[Day]):
    text = ''
    for day in days:
        if day.subjects:
            subjects = sorted(day.subjects, key=lambda s: s.subject_order)
            text += f'\n\n{calendar.day_name[day.day_id if day.day_id < 7 else day.day_id-7]}'
            for si, subject in enumerate(subjects):
                text += f'\n{subject.subject_order}) <b>{subject.subject.name}</b>({subject.subject.audience})'
    return text if text else _('Schedule is empty🫡')
