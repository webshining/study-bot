from aiogram.types import BotCommandScopeDefault

from loader import dp, bot
from data.config import ADMINS


async def on_startup():
    from database import init_days
    init_days()
    from app.commands import set_default_commands
    await set_default_commands()
    print('Bot started!')


async def on_shutdown():
    from app.commands import remove_admins_command    
    await bot.delete_my_commands(scope=BotCommandScopeDefault())
    for admin in ADMINS:
        await remove_admins_command(admin)
    print('Bot shutting down!')

    
def main():
    import app.handlers
    from app.middlewares import setup_middleware
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    setup_middleware(dp)
    dp.run_polling(bot)


if __name__ == '__main__':
    main()
