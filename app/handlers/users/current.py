from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from app.keyboards import get_update_markup
from app.routers import user_router as router
from app.states import GroupState
from database.models import Timetable
from loader import _, bot
from utils import get_current_time
from .group import _get_subject_text


@router.message(Command('current'))
async def current_handler(message: Message, user, state: FSMContext):
    if not user.group:
        await message.answer(_("You are not a member of the group yet, enter a name to create a new one:"))
        return await state.set_state(GroupState.create)
    text, markup = await _get_current_data(user.group)
    await message.answer(text, reply_markup=markup)


@router.callback_query(lambda call: call.data.startswith('current_update'))
async def current_callback_handler(call: CallbackQuery, user):
    text, markup = await _get_current_data(user.group)
    try:
        if call.inline_message_id:
            return await bot.edit_message_text(text=text, reply_markup=markup, inline_message_id=call.inline_message_id)
        await call.message.edit_text(text=text, reply_markup=markup)
    except:
        pass
    await call.answer()


async def _get_current_data(group: int):
    _current_time = get_current_time()
    timetable = await Timetable.get(group)
    day_id = _current_time.weekday() if _current_time.isocalendar().week % 2 == 0 else _current_time.weekday() + 7
    day = next(iter([i for i in timetable.days if i.day_id == day_id]))
    subject = next(iter([i for i in day.subjects if i.time_end >= _current_time]), None)
    if not subject:
        text = _('No class today')
    else:
        if _current_time >= subject.time_start:
            text = _get_subject_text(subject.subject)
            text += _('\n\nClass ends at {} in {}').format(subject.time_end.time(), subject.time_end - _current_time)
        else:
            text = (_('No class right now! Next class:\n\n{}\n\nat {} in {}')
                    .format(_get_subject_text(subject.subject), subject.time_start.time(),
                            subject.time_start - _current_time))

    markup = get_update_markup('current')
    return text, markup
