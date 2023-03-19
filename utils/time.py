from pytz import timezone
from datetime import datetime, timedelta


def current_time(time_zone: str = 'Europe/Kiev'):
    return datetime.now(timezone(time_zone))

def week_start_end(_date: datetime = current_time()):
    return (_date - timedelta(days=_date.weekday()), _date + timedelta(days=6-_date.weekday()))
