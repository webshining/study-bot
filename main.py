import asyncio

from app import setup_handlers, setup_middleware
from app.commands import set_default_commands
from database.services import init_days
from loader import bot, dp


async def on_startup():
    init_days()
    await set_default_commands()
    print('Bot started!')


async def on_shutdown():
    print('Bot shutting down!')

    
async def main():
    setup_middleware(dp)
    setup_handlers(dp)
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
