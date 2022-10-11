from datetime import date
from bson import ObjectId

from ..models import Day, days_collection
from .subjects import get_subject


def get_days(week: int = None):
    days = days_collection.find()
    days = [d for d in days]
    print(days)
    return days

def create_days(ids):
    for id in ids:
        days_collection.insert_one({'_id': ObjectId(id), 'subjects': []})
    return True

def init_days():
    if len(get_days()) != 14:
        for i in range(14):
            days_collection.insert_one({'subjects': []})
    

def edit_day(day_id: str, subjects: list[dict]):
    day = days_collection.find_one_and_update({'_id': ObjectId(day_id)}, {'$set': {
        'subjects': [{'_id': ObjectId(s['_id']), 'time_start': s['time_start'], 'time_end': s['time_end']} for s in subjects]
    }})
    return day 


def get_day_by_date(_date: date) -> Day:    
    return get_days(_date.isocalendar().week)[_date.weekday()]
