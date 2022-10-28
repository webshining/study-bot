import asyncio
from aiogram import Dispatcher
from aiogram.utils.exceptions import Throttled
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.handler import CancelHandler, current_handler

from data.config import RATE_LIMIT

class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self, limit: float = RATE_LIMIT, key_prefix: str = 'antiflood_'):
        self.rate_limit = RATE_LIMIT
        self.prefix = key_prefix
        super(ThrottlingMiddleware, self).__init__()

    async def on_process_message(self, message: Message, data: dict):
        await self._throttled(message, data)

    async def on_process_callback_query(self, call: CallbackQuery, data: dict):
        await self._throttled(call.message, data)
        
    async def _throttled(self, message: Message, throttled: Throttled):
        handler = current_handler.get()
        dispatcher = Dispatcher.get_current()
        if handler:
            limit = getattr(handler, 'throttling_rate_limit', self.rate_limit)
            key = getattr(handler, 'throttling_key', f"{self.prefix}_{handler.__name__}")
        else:
            limit = self.rate_limit
            key = f"{self.prefix}_message"
            
        try:
            await dispatcher.throttle(key, rate=limit)
        except Throttled as throttled:
            if throttled.exceeded_count <= 2:
                message = await message.reply('Too many requests!')
                await asyncio.sleep(3)
                await message.delete()
            raise CancelHandler()