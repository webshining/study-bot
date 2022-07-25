from aiogram import executor
from loader import dp, bot
from utils import logger
from config import ADMINS
from app.commands import set_default_commands


async def on_startup(dispatcher):
    logger.info('Bot started')
    await set_default_commands(bot)
    try:
        for admin in ADMINS:
            await bot.send_message(admin, 'Bot started')
    except:
        logger.error('User with this id is not exists')


async def on_shutdown(dispatcher):
    logger.warning('Bot shutting down')
    await bot.delete_my_commands()
    try:
        for admin in ADMINS:
            await bot.send_message(admin, 'Bot shutting down')
    except:
        logger.error('User with this id is not exists')


if __name__ == '__main__':
    import app.middlewares, app.handlers

    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
