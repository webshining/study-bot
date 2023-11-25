from pathlib import Path

from environs import Env

env = Env()
env.read_env()

DIR = Path(__file__).absolute().parent.parent

TELEGRAM_BOT_TOKEN = env.str('TELEGRAM_BOT_TOKEN', default=None)

OPENAI_API_KEY = env.str('OPENAI_API_KEY')

DB_USER = env.str('DB_USER', default=None)
DB_NAME = env.str('DB_NAME', default=None)
DB_PASS = env.str('DB_PASS', default=None)
DB_HOST = env.str('DB_HOST', default=None)
DB_PORT = env.int('DB_PORT', default=None)

RD_DB = env.str('RD_DB', default=None)
RD_HOST = env.str('RD_HOST', default=None)
RD_PORT = env.int('RD_PORT', default=None)
RD_PASS = env.str('RD_PASS', default=None)

I18N_DOMAIN = 'bot'
I18N_PATH = f'{DIR}/data/locales'

