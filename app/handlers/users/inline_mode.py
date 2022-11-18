import hashlib
from time import time
from aiogram.types import InlineQuery, InputTextMessageContent, InlineQueryResultArticle

from loader import dp
from .current import _get_current_data
from .schedule import _get_schedule_data
from .subjects import _get_subjects_data
from .lists import _get_lists_data


@dp.inline_query()
async def current_inline_handler(query: InlineQuery):
    schedule_text, schedule_marup = _get_schedule_data()
    schedule = InlineQueryResultArticle(
        id=hashlib.md5(f'{query}{time()}'.encode()).hexdigest(),
        thumb_url='https://cdn-icons-png.flaticon.com/512/1001/1001279.png',
        title=f'Schedule',
        description='Find out the timetable',
        input_message_content=InputTextMessageContent(message_text=schedule_text),
        reply_markup=schedule_marup
    )
    current_text, current_markup = _get_current_data()
    current = InlineQueryResultArticle(
        id=hashlib.md5(f'{query}{time()}'.encode()).hexdigest(),
        thumb_url='https://cdn-icons-png.flaticon.com/512/6557/6557160.png',
        title=f'Current subject',
        description='Get current info',
        input_message_content=InputTextMessageContent(message_text=current_text),
        reply_markup=current_markup
    )
    subjects_text, subjects_markup = _get_subjects_data()
    subjects = InlineQueryResultArticle(
        id=hashlib.md5(f'{query}{time()}'.encode()).hexdigest(),
        thumb_url='https://cdn-icons-png.flaticon.com/512/5436/5436691.png',
        title=f'Subjects info',
        description='Get subjects info',
        input_message_content=InputTextMessageContent(message_text=subjects_text),
        reply_markup=subjects_markup
    )
    lists_text, lists_markup = _get_lists_data('Select a list to view:', 'lists_get')
    lists = InlineQueryResultArticle(
        id=hashlib.md5(f'{query}{time()}'.encode()).hexdigest(),
        thumb_url='https://cdn-icons-png.flaticon.com/512/5814/5814457.png',
        title=f'Get lists',
        description='Get lists info',
        input_message_content=InputTextMessageContent(message_text=lists_text),
        reply_markup=lists_markup
    )
    await query.answer(results=[schedule, current, subjects, lists], cache_time=1)