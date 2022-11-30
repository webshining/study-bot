from pathlib import Path
from decouple import config, Csv


DIR = Path(__file__).absolute().parent.parent

TELEGRAM_BOT_TOKEN = config('TELEGRAM_BOT_TOKEN', cast=str)

ADMINS = config('ADMINS', default=[], cast=Csv(cast=int))

DB_NAME = config('DB_NAME', cast=str, default=None)
DB_USER = config('DB_USER', cast=str, default=None)
DB_PASS = config('DB_PASS', cast=str, default=None)
DB_HOST = config('DB_HOST', cast=str, default=None)
DB_PORT = config('DB_PORT', cast=int, default=None)

RD_DB = config('RD_DB', cast=str, default=None)
RD_HOST = config('RD_HOST', cast=str, default=None)
RD_PORT = config('RD_PORT', cast=int, default=None)
RD_PASS = config('RD_PASS', cast=str, default=None)

I18N_DOMAIN = 'bot'
I18N_PATH = f'{DIR}/data/locales'
