from datetime import date

from ..models import Day


def get_days(week: int = None) -> list[Day]:
    days = Day.select()
    if week:
        days = days[8:] if week % 2 == 0 else days[:7]
    return days


def get_day_by_date(date: date) -> Day:
    day = get_days(date.isocalendar().week)[date.weekday()]
    return day


def create_day(day_id: int) -> Day:
    day = Day.create(day_id=day_id)
    return day


def init_days():
    if len(get_days()) < 14:
        for i in range(14):
            create_day(i)
    return True
