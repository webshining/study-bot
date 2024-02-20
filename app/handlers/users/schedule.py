from datetime import timedelta

from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from app.keyboards import get_week_markup
from app.routers import user_router as router
from app.states import GroupState
from database.models import Timetable, TimetableDay
from loader import _, bot
from utils import get_current_time
from utils import weekdays


@router.message(Command('schedule'))
async def schedule_handler(message: Message, user, state: FSMContext):
    if not user.group:
        await message.answer(_("You are not a member of the group yet, enter a name to create a new one:"))
        return await state.set_state(GroupState.create)
    text, markup = await _get_schedule_data(user.group)
    await message.answer(text=text, reply_markup=markup)


@router.callback_query(lambda call: call.data.startswith('schedule'))
async def schedule_callback(call: CallbackQuery, user):
    text, markup = await _get_schedule_data(user.group, call.data[9:])
    try:
        if call.inline_message_id:
            return await bot.edit_message_text(text=text, reply_markup=markup, inline_message_id=call.inline_message_id)
        await call.message.edit_text(text=text, reply_markup=markup)
    except TelegramBadRequest:
        pass
    await call.answer()


async def _get_schedule_data(group: int | None, shift: str = 'this'):
    _current_time = get_current_time()
    if shift == 'next':
        _current_time += timedelta(weeks=1)
    markup = get_week_markup('schedule', shift)
    if not group:
        return _('Schedule is empty🫡'), markup
    else:
        timetable = await Timetable.get(group)
    text = _get_schedule_text(timetable.days[:7] if _current_time.isocalendar().week % 2 == 0 else timetable.days[7:])
    return text, markup


def _get_schedule_text(days: list[TimetableDay]):
    text = ''
    for day in days:
        if day.subjects:
            day_id = day.day_id
            text += f'\n\n{weekdays[day_id if day_id <= 6 else day_id - 1]}'
            for i, subject in enumerate(day.subjects):
                text += f'\n{i + 1}) <b>{subject.subject.name}</b>({subject.subject.audience})'
    return text or _('Schedule is empty🫡')
