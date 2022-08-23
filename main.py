from aiogram import executor


if __name__ == '__main__':
    import app.handlers
    executor.start_polling(app.handlers.dp)
