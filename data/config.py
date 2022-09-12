from environs import Env

env = Env()
env.read_env()


TELEGRAM_BOT_TOKEN = env.str('TELEGRAM_BOT_TOKEN', None)

MONGODB_URL = env.str('MONGODB_URL', None)
