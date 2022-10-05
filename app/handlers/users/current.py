from pytz import timezone
from datetime import datetime
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Command

from loader import dp, bot
from database.services import get_day_by_date
from app.keyboards import get_update_makrup


@dp.message_handler(Command('current'))
async def current_handler(message: Message):
    text, markup = _get_current_data()
    await message.answer(text, reply_markup=markup)


@dp.callback_query_handler(lambda call: call.data.startswith('current'))
async def current_callback_handler(call: CallbackQuery):
    await call.answer()
    text, markup = _get_current_data()
    try:
        if call.inline_message_id:
            await bot.edit_message_text(text, message_id=call.inline_message_id, inline_message_id=call.inline_message_id, reply_markup=markup)
        else:
            await bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=markup)
    except:
        pass


def _get_current_data():
    current_time = datetime.now(timezone('Europe/Kiev'))
    time = current_time.time().strftime('%H:%M:%S')
    day = get_day_by_date(current_time)
    subjects = day.subjects
    subject_now = [s for s in subjects if s.time_end >= time]
    if time >= subjects[-1].time_end:
        text = f'Classes are over!'
    elif time >= subject_now[0].time_start:
        text = f'Now class of <b>{subject_now[0].name}</b>\nTeacher: <b>{subject_now[0].teacher}</b>'
        text += f'\nAudience: <b>{subject_now[0].audience}</b>' if subject_now[0].audience else ''
        text += f'\n\n<b>{subject_now[0].info}</b>' if subject_now[0].info else ''
        text += f'\nClass ends at {subject_now[0].time_end}'
    else:
        text = f'Break now! Next class: <b>{subject_now[0].name}</b> at {subject_now[0].time_start}'
    
    markup = get_update_makrup('current')
    return text, markup