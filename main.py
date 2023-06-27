import asyncio

from aiogram.types import BotCommandScopeDefault

from app import setup_handlers, setup_middlewares
from loader import bot, dp


async def on_startup():
    from app.commands import set_default_commands
    await set_default_commands()
    print('Bot started!')


async def on_shutdown():
    print('Bot shutting down!')
    await bot.delete_my_commands(scope=BotCommandScopeDefault())
    
    
async def main():
    setup_middlewares()
    setup_handlers(dp)
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
