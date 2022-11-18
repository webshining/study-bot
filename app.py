from aiogram.types import BotCommandScopeDefault

from loader import dp, bot


async def on_startup():
    from app.commands import set_default_commands
    await set_default_commands()
    print('Bot started!')


async def on_shutdown():
    print('Bot shutting down!')
    await bot.delete_my_commands(scope=BotCommandScopeDefault())
    
    
def main():
    import app.middlewares
    import app.handlers
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    dp.run_polling(bot)


if __name__ == '__main__':
    main()
