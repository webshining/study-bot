from aiogram.types import (InlineQuery, InlineQueryResultArticle,
                           InputTextMessageContent)

from loader import _, dp

from .call_schedule import _get_call_schedule_data
from .current_lesson import _get_current_lesson_data
from .schedule import _get_schedule_data


@dp.inline_query()
async def _inline(query: InlineQuery):
    schedule_text, schedule_marup = _get_schedule_data()
    schedule = InlineQueryResultArticle(
        id=1,
        title=f'Schedule',
        description='get week timetable',
        input_message_content=InputTextMessageContent(message_text=schedule_text),
        reply_markup=schedule_marup,
    )
    call_schedule_text = _get_call_schedule_data()
    call_schedule = InlineQueryResultArticle(
        id=2,
        title=f'Call schedule',
        description='get call timetable',
        input_message_content=InputTextMessageContent(message_text=call_schedule_text),
    )
    current_lesson_text, current_lesson_markup = _get_current_lesson_data()
    current_lesson = InlineQueryResultArticle(
        id=3,
        title=f'Current lesson',
        description='get current lesson',
        input_message_content=InputTextMessageContent(message_text=current_lesson_text),
        reply_markup=current_lesson_markup
    )
    
    await query.answer(results=[schedule, call_schedule, current_lesson], cache_time=1)