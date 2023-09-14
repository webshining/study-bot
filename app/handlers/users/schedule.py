from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from app.keyboards import week_markup
from app.routers import user_router as router
from loader import _, bot
from utils import (Day, get_current_time, get_timetable, timedelta,
                   week_start_end, weekdays)

from .select_group import group_handler


@router.message(Command('schedule'))
async def schedule_handler(message: Message, group_id, state: FSMContext):
    if not group_id:
        return await group_handler(message, state, _get_schedule_data)
    text, markup = _get_schedule_data(group_id)
    await message.answer(text, reply_markup=markup)

@router.callback_query(lambda call: call.data.startswith('schedule'))
async def schedule_callback(call: CallbackQuery, group_id):
    if not group_id:
        return await call.answer(_("You haven't selected a group yet🫡"))
    text, markup = _get_schedule_data(group_id, call.data[9:])
    try:
        if call.inline_message_id:
            return await bot.edit_message_text(text=text, reply_markup=markup, inline_message_id=call.inline_message_id)
        await call.message.edit_text(text=text, reply_markup=markup, inline_message_id=call.inline_message_id)
    except:
        pass

def _get_schedule_data(group_id: int, shift: str = 'this') -> (str, any):
    date = get_current_time()
    if shift == 'next':
        date += timedelta(weeks=1)
    timetable = get_timetable(group_id, week_start_end(date))
    if timetable is None:
        text = _("It seems the servers are not responding, and there is no saved data for you🫡")
    elif timetable:
        text = _get_schedule_text(timetable)
    else: 
        text = _("Schedule is empty🫡")
    markup = week_markup('schedule', shift)
    return text, markup
    
def _get_schedule_text(timetable: list[Day]):
    text = ''
    for day in timetable:
        if day.lessons:
            text += f'\n\n{weekdays[day.date.weekday()]}'
            for lesson in day.lessons:
                period = lesson.periods[0]
                teachersName = ', '.join([p.teachersName for p in lesson.periods])    
                text += f'\n{lesson.number}) <b>{period.disciplineFullName}</b>\n({teachersName})'
    return text