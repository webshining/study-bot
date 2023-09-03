from aiogram.types import (InlineQuery, InlineQueryResultArticle,
                           InputTextMessageContent)

from app.routers import user_router as router
from loader import _

from .call_schedule import _get_call_schedule_data
from .current_lesson import _get_current_lesson_data
from .schedule import _get_schedule_data


@router.inline_query()
async def _inline(query: InlineQuery, user):
    schedule_text, schedule_marup = _get_schedule_data(user.group_id)
    schedule = InlineQueryResultArticle(
        id='1',
        title=_('Schedule'),
        description=_('get schedule'),
        input_message_content=InputTextMessageContent(message_text=schedule_text),
        reply_markup=schedule_marup,
    )
    call_schedule_text = _get_call_schedule_data()
    call_schedule = InlineQueryResultArticle(
        id='2',
        title=_('Call schedule'),
        description=_('get call timetable'),
        input_message_content=InputTextMessageContent(message_text=call_schedule_text),
    )
    current_lesson_text, current_lesson_markup = _get_current_lesson_data(user.group_id)
    current_lesson = InlineQueryResultArticle(
        id='3',
        title=_('Current lesson'),
        description=_('get current lesson'),
        input_message_content=InputTextMessageContent(message_text=current_lesson_text),
        reply_markup=current_lesson_markup
    )
    
    await query.answer(results=[schedule, call_schedule, current_lesson], cache_time=1)