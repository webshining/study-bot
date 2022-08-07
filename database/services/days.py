from ..models import Day


def get_week(week: int):
    return list(Day.select())[:7 if week % 2 != 0 else 7:]
