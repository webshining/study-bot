from datetime import date
from bson import ObjectId
from ..models import tasks_collection, Task


async def create_task(subject: str, text: str, _date: date):
    await tasks_collection.insert_one({'subject': ObjectId(subject), 'text': text, 'date': _date})


async def get_tasks_between_date(date_start: date, date_end: date):
    tasks = tasks_collection.find({'date': {'$gte': date_start, '$lt': date_end}})
    return [Task(**t) async for t in tasks]
