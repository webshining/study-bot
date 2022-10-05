import hashlib
from time import time
from aiogram.types import InlineQuery, InputTextMessageContent, InlineQueryResultArticle

from loader import dp, bot
from .current import _get_current_data
from .schedule import _get_schedule_data

@dp.inline_handler()
async def current_inline_handler(query: InlineQuery):
    schedule_text, schedule_marup = _get_schedule_data()
    schedule = InlineQueryResultArticle(
        id=hashlib.md5(f'{query}{time()}'.encode()).hexdigest(),
        thumb_url='https://cdn-icons-png.flaticon.com/512/1001/1001279.png',
        title=f'Schedule',
        description='Find out the timetable',
        input_message_content=InputTextMessageContent(schedule_text),
        reply_markup=schedule_marup
    )
    current_text, current_markup = _get_current_data()
    current = InlineQueryResultArticle(
        id=hashlib.md5(f'{query}{time()}'.encode()).hexdigest(),
        thumb_url='https://cdn-icons-png.flaticon.com/512/6557/6557160.png',
        title=f'Current subject',
        description='Get current info',
        input_message_content=InputTextMessageContent(current_text),
        reply_markup=current_markup
    )
    await query.answer(results=[schedule, current], cache_time=1)