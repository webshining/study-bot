from aiogram import executor, types
from utils import logger
from loader import bot, dp, i18n


async def on_startup(dispatcher):
    from database import init_days
    init_days()
    import app.middlewares, app.commands
    app.middlewares.setup_middlewares(dp)
    # await app.commands.set_default_commands()
    logger.info('Bot started!')


async def on_shutdown(dispatcher):
    logger.warning('Bot shutting down!')
    # await bot.delete_my_commands(scope=types.BotCommandScopeDefault())
    # for lang in i18n.available_locales:
    #     await bot.delete_my_commands(language_code=lang)


if __name__ == '__main__':
    import app.handlers
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown, skip_updates=True)
