from datetime import datetime
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from app.keyboards import get_update_markup
from app.routers import user_router as router
from database.services import get_day_by_date
from loader import _
from utils import get_current_time

from .subjects import _get_subject_data


@router.message(Command('current'))
async def current_handler(message: Message):
    text, markup = _get_current_data()
    await message.answer(text, reply_markup=markup)


@router.callback_query(lambda call: call.data.startswith('current_update'))
async def current_callback_handler(call: CallbackQuery):
    await call.answer()
    text, markup = _get_current_data()
    try:
        if call.inline_message_id:
            await call.message.edit_text(text=text, inline_message_id=call.inline_message_id, reply_markup=markup)
        else:
            await call.message.edit_text(text=text, reply_markup=markup)
    except:
        pass


def _get_current_data():
    _current_time = get_current_time()
    day = get_day_by_date(_current_time)
    subjects = list(day.subjects)
    if not subjects:
        text = _('No class today')
    else:
        subjects = [s for s in subjects if s.time_end >= _current_time.time()]
        subject = subjects[0] if subjects else None
        if not subjects:
            text = _('Classes are over')
        else:
            text, *other = _get_subject_data(subject.subject)
            if subject.time_start <= get_current_time().time():
                text += _("\n\nEnd at <b>{}</b> in <b>{}</b>").format(
                    subject.time_end,
                    str(datetime.combine(get_current_time().date(), subject.time_end) - _current_time).split('.')[0]
                )
            else:
                text += _("\n\nStart at <b>{}</b> in <b>{}</b>").format(
                    subject.time_start,
                    str(datetime.combine(get_current_time().date(), subject.time_start) - _current_time).split('.')[0]
                )

    markup = get_update_markup('current_update')
    return text, markup
