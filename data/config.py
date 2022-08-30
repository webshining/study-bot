from environs import Env

env = Env()
env.read_env()

TELEGRAM_BOT_TOKEN = env.str('TELEGRAM_BOT_TOKEN', None)

MONGO_URL = env.str('MONGO_URL', None)

RD_DB = env.str('RD_DB', None)
RD_PASS = env.str('RD_PASS', None)
RD_HOST = env.str('RD_HOST', None)
RD_PORT = env.int('RD_PORT', None)
