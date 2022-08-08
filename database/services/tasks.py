from datetime import date, datetime
from ..models import Task


def get_task(id: int):
    return Task.get_or_none(id=id)


def create_task(text: str, subject, _date: date):
    task = Task.create(text=text, subject=subject, date=_date)
    return task


def get_week_tasks(week: int, year: int = datetime.now().year):
    tasks = []
    return tasks
