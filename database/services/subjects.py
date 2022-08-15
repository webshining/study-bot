from datetime import date, timedelta
from ..models import Subject, Day


def get_subject(id: int):
    return Subject.get_by_id(id)


def get_subjects():
    return list(Subject.select())


def _get_day_number_by_date(_date: date) -> int:
    day = _date.weekday() + 1
    if _date.isocalendar().week % 2 == 0:
        day += 7
    return day


def get_subject_dates(id: int):
    days = [d for d in list(Day.select()) if id in [int(i) for i in d.subjects.split(',') if i.strip()]]
    today = date.today()
    dates_list = []
    for day in days:
        if day.id > _get_day_number_by_date(today):
            days_to = day.id - _get_day_number_by_date(today)
        else:
            days_to = 14 - _get_day_number_by_date(today) + day.id

        _date = today + timedelta(days=days_to)
        dates_list.append(_date)

    return sorted(dates_list)
