from aiogram import Bot, Dispatcher
from peewee import PostgresqlDatabase, SqliteDatabase

from app.middlewares.inter import i18n
from data.config import (DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER, DIR,
                         RD_DB, RD_HOST, RD_PASS, RD_PORT, TELEGRAM_BOT_TOKEN)

bot = Bot(TELEGRAM_BOT_TOKEN, parse_mode='HTML')
if RD_DB and RD_HOST and RD_PORT:
    from aiogram.fsm.storage.redis import RedisStorage
    from redis.asyncio.client import Redis
    storage = RedisStorage(Redis(db=RD_DB, host=RD_HOST, port=RD_PORT, password=RD_PASS))
else:
    from aiogram.fsm.storage.memory import MemoryStorage
    storage = MemoryStorage()
dp = Dispatcher(storage=storage)

database = SqliteDatabase(f'{DIR}/data/database.sqlite3')
if DB_NAME and DB_USER and DB_PASS and DB_HOST and DB_PORT:
    database = PostgresqlDatabase(DB_NAME, user=DB_USER, host=DB_HOST, port=DB_PORT, password=DB_PASS)

_ = i18n.gettext
