from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from utils import logger


class LoggingMiddleware(BaseMiddleware):
    @staticmethod
    async def on_process_message(message: Message, data: dict):
        if message.content_type == 'text':
            logger.debug(f'Id: {message.from_user.id} Message: {message.text}')

    @staticmethod
    async def on_process_callback_query(call: CallbackQuery, data: dict):
        logger.debug(f'Id: {call.from_user.id} Data: {call.data}')
        await call.answer('')
