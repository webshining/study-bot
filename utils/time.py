from datetime import datetime

from pytz import timezone


def str_to_time(string: str, format: str):
    return datetime.strptime(string, format)


def get_current_time(time_zone: str = 'Europe/Kiev'):
    return datetime.now(timezone(time_zone))
