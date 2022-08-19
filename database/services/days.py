from ..models import Day
from .subjects import get_subject


def get_week(week: int):
    days = [d for d in Day.select() if d.id in (range(8, 15) if week % 2 == 0 else range(1, 8))]
    return days


def get_week_subjects(week: int):
    days = get_week(week)
    days_subjects = []
    for day in days:
        subjects = [get_subject(int(s)) for s in day.subjects.split(',') if s.strip()]
        days_subjects.append(subjects)

    return days_subjects
