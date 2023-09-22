from datetime import timedelta

from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from app.keyboards import get_week_markup
from app.routers import user_router as router
from database.models import Day
from database.services import get_days
from loader import _, bot
from utils import get_current_time
from utils import weekdays


@router.message(Command('schedule'))
async def schedule_handler(message: Message):
    text, markup = _get_schedule_data()
    await message.answer(text=text, reply_markup=markup)


@router.callback_query(lambda call: call.data.startswith('schedule'))
async def schedule_callback(call: CallbackQuery):
    text, markup = _get_schedule_data(call.data[9:])
    try:
        if call.inline_message_id:
            return await bot.edit_message_text(text=text, reply_markup=markup, inline_message_id=call.inline_message_id)
        await call.message.edit_text(text=text, reply_markup=markup)
    except:
        pass
    await call.answer()


def _get_schedule_data(shift: str = 'this'):
    _current_time = get_current_time()
    if shift == 'next':
        _current_time += timedelta(weeks=1)
    days = get_days(_current_time.isocalendar().week)
    markup = get_week_markup('schedule', shift)
    if not days:
        return _('Schedule is empty🫡'), markup
    text = _get_schedule_text(days)
    return text, markup


def _get_schedule_text(days: list[Day]):
    text = ''
    for day in days:
        if day.subjects:
            day_id = day.day_id
            text += f'\n\n{weekdays[day_id if day_id <= 6 else day_id - 1]}'
            for i, subject in enumerate(day.subjects):
                text += f'\n{i + 1}) <b>{subject.subject.name}</b>({subject.subject.audience})'
    return text
