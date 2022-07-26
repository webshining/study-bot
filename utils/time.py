from pytz import timezone
from datetime import datetime


def str_to_time(string: str, format: str):
    return datetime.strptime(string, format)


def current_time(time_zone: str = 'Europe/Kiev'):
    return datetime.now(timezone(time_zone))
