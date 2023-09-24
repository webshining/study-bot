from pytz import timezone
from datetime import datetime


def get_current_time(time_zone: str = 'Europe/Kiev'):
    return datetime.now(timezone(time_zone)).replace(tzinfo=None)
