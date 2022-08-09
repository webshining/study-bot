from datetime import datetime, timedelta
from ..models import Day
from .subjects import get_subject


def get_week_subjects(week: int):
    if week % 2 == 0:
        days = [
            [
                get_subject(i) for i in [int(s) for s in d.subjects.split(',') if s != '']
            ] for d in list(Day.select())[7:]
        ]
    else:
        days = [
            [
                get_subject(i) for i in [int(s) for s in d.subjects.split(',') if s != '']
            ] for d in list(Day.select())[:7]
        ]

    return days


def edit_day(day, subjects: str):
    day = Day.get_by_id(day)
    day.subjects = subjects
    day.save()
    return day


def get_subject_days(id: int):
    days = Day.filter(Day.subjects.contains(f'{id}'))
    now = datetime.now().date()
    now_day_number = now.weekday() + 1 if now.isocalendar().week % 2 != 0 else now.weekday() + 8
    days_list = []
    for _day in days:
        day = dict()
        day['id'] = int(_day.id)

        if day['id'] > now_day_number:
            day['days_to'] = day['id'] - now_day_number
        else:
            day['days_to'] = 14 - now_day_number + day["id"]

        day['date'] = (now + timedelta(days=day['days_to']))
        day['date_string'] = day['date'].strftime('%Y-%m-%d')
        days_list.append(day)
    return sorted(days_list, key=lambda k: k['days_to'])
