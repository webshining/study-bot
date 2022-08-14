from ..models import Day
from .subjects import get_subject


def get_week_subjects(week: int):
    week = [i for i in (range(1, 8) if week % 2 != 0 else range(8, 15))]
    days = [[get_subject(int(s)) for s in d.subjects.split(',') if s.strip()] for d in Day.select() if d.id in week]
    return days


def change_subjects(id: int, subjects: str):
    day = Day.get_by_id(id)
    day.subjects = subjects
    day.save()
    return day
