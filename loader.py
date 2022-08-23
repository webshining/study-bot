import pymongo
from aiogram import Bot, Dispatcher, types
from data.config import DB_URL, TELEGRAM_BOT_TOKEN


bot = Bot(TELEGRAM_BOT_TOKEN, parse_mode=types.ParseMode.HTML, disable_web_page_preview=True)
dp = Dispatcher(bot)

client = pymongo.MongoClient(DB_URL)
database = client['study_bot']
