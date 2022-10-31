from aiogram import executor
from aiogram.types import BotCommandScopeDefault

from loader import dp, bot
from utils import logger


async def on_startup(dispatcher):
    from app.commands import set_default_commands
    await set_default_commands()
    logger.info('Bot started!')


async def on_shutdown(dispatcher):
    logger.error('Bot shutting down!')
    await bot.delete_my_commands(scope=BotCommandScopeDefault())


if __name__ == '__main__':
    import app.filters, app.middlewares, app.handlers
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
