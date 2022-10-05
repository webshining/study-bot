from aiogram import executor

from loader import dp
from utils import logger


async def on_startup(dispatcher):
    from database.services import init_days
    logger.info('Bot started!')
    init_days()


async def on_shutdown(dispatcher):
    logger.error('Bot shutting down!')


if __name__ == '__main__':
    import app.filters, app.middlewares, app.handlers
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
