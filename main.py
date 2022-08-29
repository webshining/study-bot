from aiogram import executor
from database import init_days
from loader import dp


async def on_startup(dispatcher):
    await init_days()


if __name__ == '__main__':
    import app.filters, app.middlewares, app.handlers
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
