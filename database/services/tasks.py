from datetime import date, datetime
from .subjects import get_subject
from ..models import tasks_collection, Task


async def create_task(subject_id: str, text: str, _date: date):
    subject = await get_subject(subject_id)
    await tasks_collection.insert_one({'subject': subject.dict(), 'text': text, 'date': _date})


async def get_tasks_between_date(date_start: date, date_end: date):
    tasks = tasks_collection.find({'date': {'$gte': date_start, '$lt': date_end}})
    return [Task(**t) async for t in tasks]


async def get_tasks_by_date(_date: date):
    tasks = tasks_collection.find({'date': _date})
    return [Task(**t) async for t in tasks] if tasks else []


async def get_tasks_by_week(week: int, year: int = date.today().year) -> list[list[Task]]:
    tasks = []
    for i in range(7):
        _date = datetime.fromisocalendar(year, week, i+1)
        tasks.append(await get_tasks_by_date(_date))
    return tasks
