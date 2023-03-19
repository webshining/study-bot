from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from calendar import day_name

from loader import dp, _, bot
from utils import get_timetable, get_faculties, Day, week_start_end, current_time, timedelta
from app.keyboards import select_markup, week_markup

@dp.message(Command('schedule'))
async def _schedule(message: Message, chat):
    if chat:
        text, markup = _get_schedule_data(chat)
        await message.answer(text, reply_markup=markup)
    else:
        await message.answer(_("Looks like u have not chosen a schedule.\nSelect faculty:"), reply_markup=select_markup('faculty', get_faculties(), 'fullName', 'id'))
        
@dp.callback_query(lambda call: call.data.startswith('schedule'))
async def _schedule_week(call: CallbackQuery, chat):
    text, markup = _get_schedule_data(chat, call.data[9:])
    try:
        if call.inline_message_id:
            if not chat:
                return await call.answer(_("U haven't chosen the timetable yet!"), show_alert=True)
            await bot.edit_message_text(text=text, reply_markup=markup, inline_message_id=call.inline_message_id)
        else:
            text, markup = _get_schedule_data(chat, call.data[9:])
            await call.message.edit_text(text=text, reply_markup=markup)
    except: 
        await call.answer()


def _get_schedule_data(chat, shift: str = 'this'):
    if chat:
        timetable = get_timetable(chat.groupId)
        if shift == 'next':
            timetable = get_timetable(chat.groupId, week_start_end(current_time()+timedelta(days=7)))
        markup = week_markup('schedule', shift)
        text = _get_schedule_text(timetable)
        return text, markup
    return None, None
    
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
    
        