from peewee import SqliteDatabase, PostgresqlDatabase
from aiogram import Bot, Dispatcher

from data.config import DIR, RD_DB, RD_HOST, RD_PASS, RD_PORT, TELEGRAM_BOT_TOKEN, DB_HOST, DB_PASS, DB_PORT, DB_USER, DB_NAME
from app.middlewares.inter import i18n


bot = Bot(TELEGRAM_BOT_TOKEN, parse_mode='HTML')
if RD_DB and RD_HOST and RD_PORT:
    from aiogram.fsm.storage.redis import RedisStorage
    from redis.asyncio.client import Redis
    storage = RedisStorage(Redis(db=RD_DB, host=RD_HOST, port=RD_PORT, password=RD_PASS))
else:
    from aiogram.fsm.storage.memory import MemoryStorage
    storage = MemoryStorage()
dp = Dispatcher(storage=storage)

database = SqliteDatabase('database.sqlite3', pragmas={'foreign_keys': 1})
if DB_NAME and DB_USER and DB_PASS and DB_HOST and DB_PORT:
    database = PostgresqlDatabase(DB_NAME, user=DB_USER, host=DB_HOST, port=DB_PORT, password=DB_PASS)

_ = i18n.gettext
