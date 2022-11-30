from pathlib import Path
from decouple import config, Csv


DIR = Path(__file__).absolute().parent.parent

TELEGRAM_BOT_TOKEN = config('TELEGRAM_BOT_TOKEN', cast=str)

ADMINS = config('ADMINS', default=[], cast=Csv(cast=int))

DB_NAME = config('DB_NAME', cast=str) or None
DB_USER = config('DB_USER', cast=str) or None
DB_PASS = config('DB_PASS', cast=str) or None
DB_HOST = config('DB_HOST', cast=str) or None
DB_PORT = config('DB_PORT', cast=int) or None

RD_DB = config('RD_DB', cast=str) or None
RD_HOST = config('RD_HOST', cast=str) or None
RD_PORT = config('RD_PORT', cast=int) or None
RD_PASS = config('RD_PASS', cast=str) or None

I18N_DOMAIN = 'bot'
I18N_PATH = f'{DIR}/data/locales'
