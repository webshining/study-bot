from datetime import date
from bson import ObjectId

from ..models import Day, days_collection
from .subjects import get_subject


def get_days(week: int = None):
    days = days_collection.find().sort("day_id")
    days = [{**d, 'subjects': [{**get_subject(s['_id']).dict(), **s} for s in d['subjects']]} for d in days]
    days = [Day(**d) for d in days]
    if week:
        days = days[7:] if week%2!=0 else days[:7]
    return days

def create_days(ids):
    for id in ids:
        days_collection.insert_one({'_id': ObjectId(id), 'subjects': []})
    return True

def init_days():
    if len(get_days()) != 14:
        for i in range(14):
            days_collection.insert_one({'subjects': []})
    

def edit_day(id: str, day_id: int):
    day = days_collection.find_one_and_update({'_id': ObjectId(id)}, {'$rename': {
        'id': "day_id"
    }})
    return day 


def get_day_by_date(_date: date) -> Day:    
    return get_days(_date.isocalendar().week)[_date.weekday()]
