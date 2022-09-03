from aiogram import executor
from database import init_days
from loader import dp, bot


async def on_startup(dispatcher):
    from app.middlewares import setup_middleware
    setup_middleware(dp)
    await init_days()


async def on_shutdown(dispatcher):
    await bot.delete_my_commands()


if __name__ == '__main__':
    import app.filters, app.handlers
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown, skip_updates=True)
