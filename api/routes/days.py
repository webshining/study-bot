from .. import daysRouter
from database import get_day, get_days, edit_day_subjects


@daysRouter.get('/')
async def get_days_router(week: int = None):
    days = [d.dict() for d in await get_days(week)]
    return {'days': days}


@daysRouter.get('/{id}')
async def get_day_router(id: str):
    day = await get_day(id)
    return {'day': day.dict()}
