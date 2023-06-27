from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from app.keyboards import get_update_markup
from app.routers import user_router as router
from database.services import get_day_by_date
from utils import get_current_time, str_to_time

from .subjects import _get_subject_text


@router.message(Command('current'))
async def current_handler(message: Message):
    text, markup = _get_current_data()
    await message.answer(text, reply_markup=markup)
    return


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
    return


def _get_current_data():
    _current_time = get_current_time()
    day = get_day_by_date(_current_time)
    subject_now = [s for s in day.subjects if s.time_end >= _current_time.time()] if day else []
    if not subject_now:
        text = f'Classes are over!'
    elif _current_time.time() >= subject_now[0].time_start:
        text = _get_subject_text(subject_now[0].subject)
        text += f'\n\nСlass ends at {subject_now[0].time_end}'
    else:
        text = f'No class right now! Next class: {subject_now[0].subject.name} at {subject_now[0].time_start}'

    markup = get_update_markup('current_update')
    return text, markup
