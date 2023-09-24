from datetime import date

from ..models import Day, DaySubject


def get_days(week: int = None) -> list[Day]:
    days = Day.select()
    if week:
        days = days[7:] if week % 2 == 0 else days[:7]
    return list(days)


def get_day_by_date(_date: date) -> Day:
    day = get_days(_date.isocalendar().week)[_date.weekday()]
    return day


def edit_day(id: int, subjects: list[dict]):
    subjects = [{**s, 'day': id} for s in subjects]
    days_subjects = Day.subjects.rel_model
    days_subjects.delete().where(DaySubject.day == id).execute()
    days_subjects.insert_many(subjects).execute()
    return True


def init_days():
    if len(get_days()) < 14:
        for i in range(14):
            Day.create(day_id=i)
    return True
