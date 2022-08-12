from environs import Env

env = Env()
env.read_env()

TELEGRAM_BOT_TOKEN = env.str('TELEGRAM_BOT_TOKEN', None)

DB_NAME = env.str('DB_NAME', None)
DB_USER = env.str('DB_USER', None)
DB_PASS = env.str('DB_PASS', None)
DB_HOST = env.str('DB_HOST', None)
DB_PORT = env.int('DB_PORT', None)
