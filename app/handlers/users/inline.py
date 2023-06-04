from aiogram.types import (InlineQuery, InlineQueryResultArticle,
                           InputTextMessageContent)

from loader import _, dp

from .schedule import _get_schedule_data


@dp.inline_query()
async def _inline(query: InlineQuery):
    schedule_text, schedule_marup = _get_schedule_data()
    schedule = InlineQueryResultArticle(
        id=1,
        title=f'Schedule',
        description='get week timetable',
        input_message_content=InputTextMessageContent(message_text=schedule_text),
        reply_markup=schedule_marup
    )
    
    await query.answer(results=[schedule], cache_time=1)