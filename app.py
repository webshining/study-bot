from aiogram import executor
from aiogram.types import BotCommandScopeDefault

from loader import dp, bot
from utils import logger


async def on_startup(dispatcher):
    from app.commands import set_default_commands
    await set_default_commands()
    logger.info('Bot started!')    
    from database.services import edit_day, create_days, get_days

    if len(get_days()) != 14:
        create_days([
            '633d3aa54e5ac7c0a47dcf2f',
            '633d3aa64e5ac7c0a47dcf30',
            '633d3aa64e5ac7c0a47dcf31',
            '633d3aa64e5ac7c0a47dcf32',
            '633d3aa64e5ac7c0a47dcf33',
            '633d3aa64e5ac7c0a47dcf34',
            '633d3aa64e5ac7c0a47dcf35',
            '633d3aa64e5ac7c0a47dcf36',
            '633d3aa64e5ac7c0a47dcf37',
            '633d3aa64e5ac7c0a47dcf38',
            '633d3aa64e5ac7c0a47dcf39',
            '633d3aa64e5ac7c0a47dcf3a',
            '633d3aa64e5ac7c0a47dcf3b',
            '633d3aa64e5ac7c0a47dcf3c'
        ])


        edit_day('633d3aa54e5ac7c0a47dcf2f', [

            {'_id': '633d3e67e1264e61a1988631', 'time_start': '08:20:00', 'time_end': '09:40:00'}, 

            {'_id': '633d3e67e1264e61a1988631', 'time_start': '10:05:00', 'time_end': '11:25:00'},

        ])

        edit_day('633d3aa64e5ac7c0a47dcf30', [

            {'_id': '633d3e67e1264e61a1988632', 'time_start': '08:20:00', 'time_end': '09:40:00'}, 

            {'_id': '633d3e67e1264e61a1988632', 'time_start': '10:05:00', 'time_end': '11:25:00'},

            {'_id': '633d40f6b8aeb6b820c1b891', 'time_start': '12:05:00', 'time_end': '13:25:00'}, 

            {'_id': '633d40f6b8aeb6b820c1b891', 'time_start': '13:50:00', 'time_end': '15:10:00'},

        ])

        edit_day('633d3aa64e5ac7c0a47dcf31', [

            {'_id': '633d3e67e1264e61a198862e', 'time_start': '08:20:00', 'time_end': '09:40:00'}, 

            {'_id': '633d3e67e1264e61a198862e', 'time_start': '10:05:00', 'time_end': '11:25:00'},

            {'_id': '633d3e67e1264e61a198862f', 'time_start': '12:05:00', 'time_end': '13:25:00'}, 

            {'_id': '633d3e67e1264e61a198862f', 'time_start': '13:50:00', 'time_end': '15:10:00'},

        ])

        edit_day('633d3aa64e5ac7c0a47dcf32', [])

        edit_day('633d3aa64e5ac7c0a47dcf33', [

            {'_id': '633d40f6b8aeb6b820c1b891', 'time_start': '08:20:00', 'time_end': '09:40:00'}, 

            {'_id': '633d40f6b8aeb6b820c1b891', 'time_start': '10:05:00', 'time_end': '11:25:00'},

        ])

        edit_day('633d3aa64e5ac7c0a47dcf34', [])

        edit_day('633d3aa64e5ac7c0a47dcf35', [])

        edit_day('633d3aa64e5ac7c0a47dcf36', [

            {'_id': '633d3e67e1264e61a1988631', 'time_start': '08:20:00', 'time_end': '09:40:00'}, 

            {'_id': '633d3e67e1264e61a1988631', 'time_start': '10:05:00', 'time_end': '11:25:00'},

            {'_id': '633d3e67e1264e61a198862f', 'time_start': '12:05:00', 'time_end': '13:25:00'}, 

            {'_id': '633d3e67e1264e61a198862f', 'time_start': '13:50:00', 'time_end': '15:10:00'},

        ])

        edit_day('633d3aa64e5ac7c0a47dcf37', [

            {'_id': '633d3e67e1264e61a198862e', 'time_start': '08:20:00', 'time_end': '09:40:00'}, 

            {'_id': '633d3e67e1264e61a198862e', 'time_start': '10:05:00', 'time_end': '11:25:00'},

            {'_id': '633d3e67e1264e61a1988631', 'time_start': '12:05:00', 'time_end': '13:25:00'}, 

            {'_id': '633d3e67e1264e61a1988631', 'time_start': '13:50:00', 'time_end': '15:10:00'},

        ])

        edit_day('633d3aa64e5ac7c0a47dcf38', [])

        edit_day('633d3aa64e5ac7c0a47dcf39', [

            {'_id': '633d3e67e1264e61a1988632', 'time_start': '08:20:00', 'time_end': '09:40:00'}, 

            {'_id': '633d3e67e1264e61a1988632', 'time_start': '10:05:00', 'time_end': '11:25:00'},

            {'_id': '633d3e67e1264e61a1988631', 'time_start': '12:05:00', 'time_end': '13:25:00'}, 

            {'_id': '633d3e67e1264e61a1988631', 'time_start': '13:50:00', 'time_end': '15:10:00'},

        ])

        edit_day('633d3aa64e5ac7c0a47dcf3a', [

            {'_id': '633d40f6b8aeb6b820c1b891', 'time_start': '08:20:00', 'time_end': '09:40:00'}, 

            {'_id': '633d40f6b8aeb6b820c1b891', 'time_start': '10:05:00', 'time_end': '11:25:00'},

            {'_id': '633d3e67e1264e61a1988632', 'time_start': '12:05:00', 'time_end': '13:25:00'}, 

            {'_id': '633d3e67e1264e61a1988632', 'time_start': '13:50:00', 'time_end': '15:10:00'},

        ])

        edit_day('633d3aa64e5ac7c0a47dcf3b', [])

        edit_day('633d3aa64e5ac7c0a47dcf3c', [])


async def on_shutdown(dispatcher):
    logger.error('Bot shutting down!')
    await bot.delete_my_commands(scope=BotCommandScopeDefault())


if __name__ == '__main__':
    import app.filters, app.middlewares, app.handlers
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
