from datetime import date, datetime
from ..models import Task
from .days import get_subject_days


def get_task(id: int):
    return Task.get_or_none(id=id)


def add_task(text: str, subject, day: int = 0):
    subject_days = get_subject_days(int(subject))
    if len(subject_days) > 0:
        return create_task(text, int(subject), subject_days[day]['date'])
    return False


def create_task(text: str, subject, _date: date):
    return Task.create(text=text, subject=subject, date=_date)


def get_date_tasks(_date: date):
    return list(Task.select().where(Task.date == _date))


def get_week_tasks(week: int, year: int = datetime.now().year):
    days = []
    for i in range(7):
        _date = date.fromisocalendar(year, week, i+1)
        days.append(get_date_tasks(_date))
    return days
