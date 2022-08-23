from environs import Env

env = Env()
env.read_env()

TELEGRAM_BOT_TOKEN = env.str('TELEGRAM_BOT_TOKEN', None)

DB_URL = env.str('DB_URL', None)
