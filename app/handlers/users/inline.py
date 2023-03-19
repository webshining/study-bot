from aiogram.types import InlineQuery, InputTextMessageContent, InlineQueryResultArticle


from loader import dp, _
from .schedule import _get_schedule_data
from database.models import Chat


@dp.inline_query()
async def _inline(query: InlineQuery, chat: Chat):
    schedule_text, schedule_marup = _get_schedule_data(chat) if chat else (_("U haven't chosen the timetable yet!"), None)
    schedule = InlineQueryResultArticle(
        id=1,
        title=f'Schedule',
        description='get week timetable',
        input_message_content=InputTextMessageContent(message_text=schedule_text),
        reply_markup=schedule_marup
    )
    
    await query.answer(results=[schedule], cache_time=1)