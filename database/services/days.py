from bson import ObjectId
from ..models import Day, days_collection
from .subjects import get_subject


def get_days(week: int = None):
    days = days_collection.aggregate([{'$lookup': {
        'from': 'subjects',
        'localField': 'subjects',
        'foreignField': '_id',
        'as': 'subjects'
    }}])
    days = [Day(**{'_id': d['_id'], 'subjects': [get_subject(s) for s in d['subjects']]}) for d in days]
    if week:
        days = days[7:] if week % 2 == 0 else days[-7:]
    return days


def get_day(id: str):
    day = days_collection.find_one({'_id': ObjectId(id)})
    return Day(**{'_id': day['_id'], 'subjects': [get_subject(s) for s in day['subjects']]})
