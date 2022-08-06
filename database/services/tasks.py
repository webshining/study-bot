from datetime import datetime, date
from ..models import Task, Subject


def get_task(id: int):
    return Task.get_or_none(id=id)


def get_tasks():
    return list(Task.select())


def create_task(text: str, subject: Subject, _date: date):
    return Task.create(text=text, subject=subject, date=_date)
