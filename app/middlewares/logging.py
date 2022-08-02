from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message
from utils import logger


class LoggingMiddleware(BaseMiddleware):
    @staticmethod
    async def on_process_message(message: Message, data: dict):
        if message.content_type == 'text':
            logger.debug(f'Id: {message.from_user.id} Message: {message.text}')