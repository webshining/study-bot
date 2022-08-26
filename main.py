from aiogram import executor
from database import init_days, edit_day_subjects


async def on_startup(dispatcher):
    await init_days()
    await edit_day_subjects('6308bf15bd6d31b881aaf369', ['6308bd6f330a1346b4267510', '6308a9ba83558c993c5fbdf2'])


if __name__ == '__main__':
    import app.handlers
    executor.start_polling(app.handlers.dp, on_startup=on_startup, skip_updates=True)
