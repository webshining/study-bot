from calendar import day_name

from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from app.keyboards import week_markup
from loader import _, bot, dp
from utils import Day, current_time, get_timetable, timedelta, week_start_end


@dp.message(Command('schedule'))
async def _schedule(message: Message):
    text, markup = _get_schedule_data()
    await message.answer(text, reply_markup=markup)
        
@dp.callback_query(lambda call: call.data.startswith('schedule'))
async def _schedule_week(call: CallbackQuery):
    text, markup = _get_schedule_data(call.data[9:])
    try:
        if call.inline_message_id:
            await bot.edit_message_text(text=text, reply_markup=markup, inline_message_id=call.inline_message_id)
        else:
            text, markup = _get_schedule_data(call.data[9:])
            await call.message.edit_text(text=text, reply_markup=markup)
    except: 
        await call.answer()


def _get_schedule_data(shift: str = 'this'):
    timetable = get_timetable()
    if shift == 'next':
        timetable = get_timetable(week_start_end(current_time()+timedelta(days=7)))
    markup = week_markup('schedule', shift)
    text = _get_schedule_text(timetable)
    return text, markup
    
def _get_schedule_text(timetable: list[Day]):
    text = ''
    for day in timetable:
        if day.lessons:
            text += f'\n\n{day_name[day.date.weekday()]}'
            for lesson in day.lessons:
                period = lesson.periods[0]
                text += f'\n{lesson.number}) <b>{period.disciplineFullName}</b>({period.classroom})'
    if not text: text = _("Schedule is empty!")
    return text
    
        