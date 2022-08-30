import motor.motor_asyncio
from aiogram import Bot, Dispatcher, types
from data.config import MONGO_URL, TELEGRAM_BOT_TOKEN, RD_HOST, RD_PORT, RD_DB, RD_PASS


bot = Bot(TELEGRAM_BOT_TOKEN, parse_mode=types.ParseMode.HTML, disable_web_page_preview=True)
if RD_HOST and RD_DB and RD_PORT:
    from aiogram.contrib.fsm_storage.redis import RedisStorage2
    storage = RedisStorage2(RD_HOST, RD_PORT, RD_DB, RD_PASS)
else:
    from aiogram.contrib.fsm_storage.memory import MemoryStorage
    storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
database = client.study_bot
