import asyncio

from app import setup_handlers, setup_middleware
from app.commands import set_default_commands
from loader import bot, dp
from utils import logger


async def on_startup():
    await set_default_commands()
    logger.info("Bot started!")


async def on_shutdown():
    logger.info('Bot shutting down!')

    
def main():
    setup_middleware(dp)
    setup_handlers(dp)
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    dp.run_polling(bot)


if __name__ == '__main__':
    main()
    
