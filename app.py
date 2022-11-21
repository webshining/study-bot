from aiogram.types import BotCommandScopeDefault

from loader import dp, bot


async def on_startup():
    # from app.commands import set_default_commands
    # await set_default_commands()
    from database import init_days
    init_days()
    print('Bot started!')


async def on_shutdown():
    # await bot.delete_my_commands(scope=BotCommandScopeDefault())
    print('Bot shutting down!')

    
def main():
    import app.middlewares
    import app.handlers
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    dp.run_polling(bot)


if __name__ == '__main__':
    main()
