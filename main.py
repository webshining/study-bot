from aiogram import executor
from database import Subject, File, Day, init_days
from loader import database


async def on_startup(dispatcher):
    database.create_tables([Subject, File, Day])
    init_days()


if __name__ == '__main__':
    import app.handlers
    executor.start_polling(app.handlers.dp, on_startup=on_startup)
