import urllib.parse
from pathlib import Path

from environs import Env

env = Env()
env.read_env()

DIR = Path(__file__).absolute().parent.parent

TIMEZONE = env.str('TIMEZONE', 'Europe/Kyiv')

TELEGRAM_BOT_TOKEN = env.str('TELEGRAM_BOT_TOKEN', None)

MONGO_DB = env.str("MONGO_DB", "bot")
MONGO_HOST = env.str("MONGO_HOST", "localhost")
MONGO_PORT = env.int("MONGO_PORT", 27017)
MONGO_USER = env.str("MONGO_USER", None)
MONGO_PASS = env.str("MONGO_PASS", None)

MONGO_URI = env.str('MONGO_URL', f"mongodb://{MONGO_HOST}:{MONGO_PORT}")
if MONGO_USER and MONGO_PASS:
    MONGO_URI = f'mongodb://{urllib.parse.quote(MONGO_USER)}:{urllib.parse.quote(MONGO_PASS)}@{MONGO_HOST}:{MONGO_PORT}'

RD_DB = env.int("RD_DB", 5)
RD_HOST = env.str("RD_HOST", "localhost")
RD_PORT = env.int("RD_PORT", 6379)

RD_URI = env.str("RD_URI", f'redis://{RD_HOST}:{RD_PORT}/{RD_DB}')

I18N_DOMAIN = 'bot'
I18N_PATH = f'{DIR}/data/locales'
