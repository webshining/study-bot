from datetime import datetime, date
from ..models import Day
from .subjects import get_subject
from .tasks import get_date_tasks


def edit_day(day, subjects: str):
    day = Day.get_by_id(day)
    day.subjects = subjects
    day.save()
    return day


def get_week_subjects(week: int):
    if week % 2 == 0:
        days = list(Day.select())[7:]
    else:
        days = list(Day.select())[:7]

    week = [
        [
            get_subject(i) for i in [int(s) for s in d.subjects.split(',') if s != '']
        ] for d in days
    ]

    return week


def get_week_tasks(week: int, year: int = datetime.now().year):
    days = []
    for i in range(7):
        _date = date.fromisocalendar(year, week, i + 1)
        days.append(get_date_tasks(_date))
    return days


def get_subject_days(id: int):
    days = Day.filter(Day.subjects.contains(f'{id}'))
    now = datetime.now().date()
    now_day_number = now.weekday() + (1 if now.isocalendar().week % 2 != 0 else 8)
    days_list = []
    for _day in days:
        day = dict
        day['id'] = _day.id
        if _day.id > now_day_number:
            day['days_to'] = day['id'] - now_day_number
        else:
            day['days_to'] = 14 - now_day_number + day["id"]
