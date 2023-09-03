from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from app.keyboards import week_markup
from app.routers import user_router as router
from loader import _, bot
from utils import (Day, get_current_time, get_timetable, timedelta,
                   week_start_end)

from .select_group import group_handler


@router.message(Command('schedule'))
async def _schedule(message: Message, group_id):
    if not group_id:
        return await group_handler(message)
    text, markup = _get_schedule_data(group_id)
    await message.answer(text, reply_markup=markup)
        
@router.callback_query(lambda call: call.data.startswith('schedule'))
async def _schedule_week(call: CallbackQuery, group_id):
    if not group_id:
        return await group_handler(call.message)
    text, markup = _get_schedule_data(group_id, call.data[9:])
    start_end = week_start_end(get_current_time()+timedelta(days=7)) if call.data[9:] == 'next' else week_start_end()
    await call.answer(' <-> '.join([str(i.date()) for i in start_end]))
    try:
        if call.inline_message_id:
            return await bot.edit_message_text(text=text, reply_markup=markup, inline_message_id=call.inline_message_id)
        await call.message.edit_text(text=text, reply_markup=markup, inline_message_id=call.inline_message_id)
    except:
        pass

def _get_schedule_data(group_id: int, shift: str = 'this') -> (str, any):
    timetable = get_timetable(group_id)
    if shift == 'next':
        timetable = get_timetable(group_id, week_start_end(get_current_time()+timedelta(days=7)))
    markup = week_markup('schedule', shift)
    text = _get_schedule_text(timetable)
    return text, markup
    
def _get_schedule_text(timetable: list[Day]):
    text = ''
    weekdays = _('Monday Tuesday Wednesday Thursday Friday Saturday Sunday')
    for day in timetable:
        if day.lessons:
            text += f'\n\n{weekdays.split(" ")[day.date.weekday()]}'
            for lesson in day.lessons:
                period = lesson.periods[0]
                teachersName = ', '.join([p.teachersName for p in lesson.periods])    
                text += f'\n{lesson.number}) <b>{period.disciplineFullName}</b>\n({teachersName})'
    if not text: text = _("Schedule is empty🫡")
    return text
    
        