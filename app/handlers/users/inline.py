from aiogram.types import (InlineQuery, InlineQueryResultArticle,
                           InputTextMessageContent)

from app.routers import user_router as router
from loader import _

from .call_schedule import _get_call_schedule_data
from .current_lesson import _get_current_lesson_data
from .schedule import _get_schedule_data
from .tasks import _get_tasks_data


@router.inline_query()
async def inline_handler(query: InlineQuery, group_id):
    if not group_id:
        no_group = InlineQueryResultArticle(
            id='1',
            title=_('You haven\'t selected a group yet🫡'),
            input_message_content=InputTextMessageContent(message_text=_('You haven\'t selected a group yet🫡')),
        )
        await query.answer(results=[no_group], cache_time=1)
    else:
        schedule_text, schedule_markup = await _get_schedule_data(group_id)
        schedule = InlineQueryResultArticle(
            id='1',
            title=_('Schedule'),
            description=_('get schedule'),
            input_message_content=InputTextMessageContent(message_text=schedule_text),
            reply_markup=schedule_markup,
        )
        call_schedule_text = _get_call_schedule_data()
        call_schedule = InlineQueryResultArticle(
            id='2',
            title=_('Call schedule'),
            description=_('get call schedule'),
            input_message_content=InputTextMessageContent(message_text=call_schedule_text),
        )
        current_lesson_text, current_lesson_markup = await _get_current_lesson_data(group_id)
        current_lesson = InlineQueryResultArticle(
            id='3',
            title=_('Current lesson'),
            description=_('get current lesson'),
            input_message_content=InputTextMessageContent(message_text=current_lesson_text),
            reply_markup=current_lesson_markup
        )
        tasks_text, tasks_markup = await _get_tasks_data(group_id)
        tasks = InlineQueryResultArticle(
            id='4',
            title=_('Tasks'),
            description=_('get tasks'),
            input_message_content=InputTextMessageContent(message_text=tasks_text),
            reply_markup=tasks_markup
        )

        await query.answer(results=[schedule, call_schedule, current_lesson, tasks], cache_time=1)
