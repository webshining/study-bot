from datetime import datetime, timedelta

from pytz import timezone


def get_current_time(time_zone: str = 'Europe/Kiev'):
    return datetime.now(timezone(time_zone)).replace(tzinfo=None)

def week_start_end(_date: datetime = get_current_time()):
    return (_date - timedelta(days=_date.weekday()), _date + timedelta(days=6-_date.weekday()))
