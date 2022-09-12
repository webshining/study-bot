from pymongo import MongoClient
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data.config import MONGODB_URL, TELEGRAM_BOT_TOKEN


bot = Bot(TELEGRAM_BOT_TOKEN, parse_mode=types.ParseMode.HTML, disable_web_page_preview=True)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


client = MongoClient(MONGODB_URL)
db = client['StudyBot']
