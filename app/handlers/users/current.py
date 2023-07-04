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
    subjects = day.subjects
    if not subjects:
        text = _('No class today')
    else:
        subjects = [s for s in subjects if s.time_end >= _current_time.time()]
        if not subjects:
            text = _('Classes are over')
        elif _current_time >= subjects[0].time_start:
            text, *other = _get_subject_data(subjects[0].subject)
            text += _('\n\nClass ends at {} in {}').format(subjects[0].time_end, subjects[0].time_end - _current_time)
        else:
            text = _('No class right now! Next class: {} at {} in {}').format(subjects[0].subject.name, subjects[0].time_start, subjects[0].time_start - _current_time)
    
    markup = get_update_markup('current_update')
    return text, markup
