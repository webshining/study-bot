import hashlib
from time import time

from aiogram.types import (InlineQuery, InlineQueryResultArticle,
                           InputTextMessageContent)

from app.routers import user_router as router
from loader import _

from .current import _get_current_data
from .schedule import _get_schedule_data
from .subjects import _get_subjects_data


@router.inline_query()
async def current_inline_handler(query: InlineQuery):
    schedule_text, schedule_markup = _get_schedule_data()
    schedule = InlineQueryResultArticle(
        id=hashlib.md5(f'{query}{time()}1'.encode()).hexdigest(),
        thumb_url='https://cdn-icons-png.flaticon.com/512/1001/1001279.png',
        title=_('Get schedule'),
        description=_('Find out the timetable'),
        input_message_content=InputTextMessageContent(message_text=schedule_text),
        reply_markup=schedule_markup
    )
    current_text, current_markup = _get_current_data()
    current = InlineQueryResultArticle(
        id=hashlib.md5(f'{query}{time()}2'.encode()).hexdigest(),
        thumb_url='https://cdn-icons-png.flaticon.com/512/6557/6557160.png',
        title=_('Current subject'),
        description=_('Get current info'),
        input_message_content=InputTextMessageContent(message_text=current_text),
        reply_markup=current_markup
    )
    subjects_text, subjects_markup = _get_subjects_data()
    subjects = InlineQueryResultArticle(
        id=hashlib.md5(f'{query}{time()}3'.encode()).hexdigest(),
        thumb_url='https://cdn-icons-png.flaticon.com/512/5436/5436691.png',
        title=_('Subjects info'),
        description=_('Get subjects info'),
        input_message_content=InputTextMessageContent(message_text=subjects_text),
        reply_markup=subjects_markup
    )
    await query.answer(results=[schedule, current, subjects], cache_time=1)
