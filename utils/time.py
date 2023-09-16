from datetime import datetime

from pytz import timezone

from data.config import TIMEZONE


def get_current_time(time_zone: str = TIMEZONE) -> datetime:
    return datetime.now(timezone(time_zone)).replace(tzinfo=None)


def str_to_time(string: str, format: str) -> datetime:
    return datetime.combine(get_current_time().date(), datetime.strptime(string, format).time())
