from environs import Env

env = Env()
env.read_env()

ADMINS = env.list('ADMINS', subcast=int, default=[])
TELEGRAM_BOT_TOKEN = env.str('TELEGRAM_BOT_TOKEN')

DB_NAME = env.str('DB_NAME', None)
DB_USER = env.str('DB_USER', None)
DB_PASSWORD = env.str('DB_PASSWORD', None)
DB_HOST = env.str('DB_HOST', None)
DB_PORT = env.int('DB_PORT', default=None)

I18N_DOMAIN = 'mybot'
