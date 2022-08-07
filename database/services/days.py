from ..models import Day


def get_week(week: int):
    if week % 2 == 0:
        return list(Day.select())[7:]
    else:
        return list(Day.select())[:7]
