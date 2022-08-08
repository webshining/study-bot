from ..models import Day


def get_week_subjects(week: int):
    return [d.subjects for d in (list(Day.select())[:7] if week % 2 != 0 else list(Day.select())[7:])]
