from aiogram import executor
from database import init_days


async def on_startup(dispatcher):
    await init_days()


if __name__ == '__main__':
    import app.handlers
    executor.start_polling(app.handlers.dp, on_startup=on_startup, skip_updates=True)
