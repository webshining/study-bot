from pathlib import Path
from decouple import config


DIR = Path(__file__).absolute().parent.parent

TELEGRAM_BOT_TOKEN = config('TELEGRAM_BOT_TOKEN', default=None)

ADMINS = config('ADMINS', default='', cast=lambda v: [int(s.strip()) for s in v.split(',')])

DB_NAME = config('DB_NAME', default=None)
DB_USER = config('DB_USER', default=None)
DB_PASS = config('DB_PASS', default=None)
DB_HOST = config('DB_HOST', default=None)
DB_PORT = config('DB_PORT', default=None)
DB_PORT = int(DB_PORT) if DB_PORT else None

RD_DB = config('RD_DB', default=None)
RD_HOST = config('RD_HOST', default=None)
RD_PORT = config('RD_PORT', default=None)
RD_PORT = int(RD_PORT) if RD_PORT else None
RD_PASS = config('RD_PASS', default=None)

I18N_DOMAIN = 'bot'
I18N_PATH = f'{DIR}/data/locales'
