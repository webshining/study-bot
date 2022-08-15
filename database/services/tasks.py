from datetime import date
from .subjects import get_subject_dates
from ..models import Task, Subject


def get_tasks_by_date(_date: date):
    return list(Task.select().where(Task.date == _date))


def get_tasks_between_dates(date_start: date, date_end: date):
    return list(Task.select().where(Task.date.between(date_start, date_end)))


def get_tasks_by_week(week: int, year: int = date.today().year):
    tasks = []
    for i in range(7):
        tasks.append(get_tasks_by_date(date.fromisocalendar(year, week, i + 1)))
    return tasks


def create_task(text: str, subject: int, _date: date):
    return Task.create(text=text, subject=subject, date=_date)


def add_task(text: str, subject: int, day: int = 0):
    _date = get_subject_dates(subject)[day]
    return create_task(text, subject, _date)
