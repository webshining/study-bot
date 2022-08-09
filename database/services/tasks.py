from datetime import date, datetime
from ..models import Task


def get_task(id: int):
    return Task.get_or_none(id=id)


def create_task(text: str, subject, _date: date):
    return Task.create(text=text, subject=subject, date=_date)


def get_date_tasks(_date: date):
    return list(Task.select().where(Task.date == _date))
