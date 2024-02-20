from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.utils.i18n import I18n
from motor.motor_tornado import MotorClient
from redis.asyncio.client import Redis

from data.config import MONGO_URI, TELEGRAM_BOT_TOKEN, I18N_DOMAIN, I18N_PATH, RD_URI, MONGO_DB

bot = Bot(TELEGRAM_BOT_TOKEN, parse_mode='HTML')

storage = RedisStorage(Redis.from_url(RD_URI))
dp = Dispatcher(storage=storage)

client = MotorClient(MONGO_URI)
db = client[MONGO_DB]

i18n = I18n(path=I18N_PATH, domain=I18N_DOMAIN)
_ = i18n.gettext
