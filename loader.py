from aiogram import Bot, Dispatcher, types
from data.config import TELEGRAM_BOT_TOKEN, DB_USER, DB_PASS, DB_NAME, DB_HOST, DB_PORT, RD_DB, RD_HOST, RD_PORT, RD_PASS
from utils import logger
from app.middlewares import i18n
_ = i18n.gettext

# Init bot and storage
bot = Bot(TELEGRAM_BOT_TOKEN, disable_web_page_preview=True, parse_mode=types.ParseMode.HTML)
if RD_DB and RD_HOST and RD_PORT:
    from aiogram.contrib.fsm_storage.redis import RedisStorage2

    storage = RedisStorage2(RD_HOST, RD_PORT, RD_DB, RD_PASS if RD_PASS else None)
else:
    from aiogram.contrib.fsm_storage.memory import MemoryStorage

    storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# Setup startup and shutdown notify
async def on_startup(dispatcher):
    from app.middlewares import setup_middlewares
    from app.commands import set_default_commands
    await set_default_commands()
    setup_middlewares(dp)
    logger.info('Bot started!')


async def on_shutdown(dispatcher):
    logger.warning('Bot shutting down!')
    await bot.delete_my_commands(scope=types.BotCommandScopeDefault())


# Init database type
if DB_USER and DB_NAME and DB_PASS and DB_HOST and DB_PORT:
    from peewee import PostgresqlDatabase

    database = PostgresqlDatabase(DB_NAME, host=DB_HOST, port=DB_PORT, password=DB_PASS, user=DB_USER)
else:
    from peewee import SqliteDatabase

    database = SqliteDatabase('./data/database.sqlite')
