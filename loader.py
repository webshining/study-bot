from aiogram import Bot, Dispatcher
from aiogram.utils.i18n import I18n
from peewee import PostgresqlDatabase, SqliteDatabase
from redis.asyncio import Redis
from openai import AsyncOpenAI


from data.config import (DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER, DIR,
                         I18N_DOMAIN, I18N_PATH, RD_DB, RD_HOST, RD_PASS,
                         RD_PORT, TELEGRAM_BOT_TOKEN, OPENAI_API_KEY)

redis = Redis(db=RD_DB, host=RD_HOST, port=RD_PORT, password=RD_PASS, auto_close_connection_pool=True)
bot = Bot(TELEGRAM_BOT_TOKEN, parse_mode='HTML')
if RD_DB and RD_HOST and RD_PORT:
    from aiogram.fsm.storage.redis import RedisStorage
    storage = RedisStorage(redis)
else:
    from aiogram.fsm.storage.memory import MemoryStorage
    storage = MemoryStorage()
dp = Dispatcher(storage=storage)

database = SqliteDatabase(f'database.sqlite3')
if DB_NAME and DB_USER and DB_PASS and DB_HOST and DB_PORT:
    database = PostgresqlDatabase(DB_NAME, user=DB_USER, host=DB_HOST, port=DB_PORT, password=DB_PASS)

i18n = I18n(path=I18N_PATH, domain=I18N_DOMAIN)
_ = i18n.gettext

openai_client = AsyncOpenAI(api_key=OPENAI_API_KEY)
