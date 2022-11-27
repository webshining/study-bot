from pytz import timezone
from datetime import datetime


def current_time(time_zone: str = 'Europe/Kiev'):
    return datetime.now(timezone(time_zone))
