import asyncio
from database import init_days


async def handler():
    await init_days()


ioloop = asyncio.new_event_loop()
asyncio.set_event_loop(ioloop)
ioloop.run_until_complete(handler())
