from aiogram import Bot, Dispatcher, types
from peewee import SqliteDatabase, PostgresqlDatabase
from data.config import DB_HOST, DB_PASS, DB_USER, DB_PORT, DB_NAME, TELEGRAM_BOT_TOKEN


bot = Bot(TELEGRAM_BOT_TOKEN, parse_mode=types.ParseMode.HTML, disable_web_page_preview=True)
dp = Dispatcher(bot)

if DB_HOST and DB_PASS and DB_USER and DB_PORT and DB_NAME:
    database = PostgresqlDatabase(DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
else:
    database = SqliteDatabase('data/database.sqlite3')
