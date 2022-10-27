from datetime import date
from bson import ObjectId

from ..models import Day, days_collection


def get_days(week: int = None):
    days = days_collection.aggregate([
        {"$unwind": {"path": "$subjects", "preserveNullAndEmptyArrays": True}},
        {"$lookup": {"from": "subjects", "localField": "subjects._id", "foreignField": "_id", "as": "subjects.subject"}},
        {"$unwind": {"path": "$subjects.subject", "preserveNullAndEmptyArrays": True}},
        {"$group": {"_id": "$_id", "subjects": {"$push": "$subjects"}, "day_id": {"$first": "$day_id"}}},
        {"$sort": {"day_id": 1}},
        {"$project": {"subjects": {"$cond": {"if": {"$eq": ["$subjects", [{}]]}, "then": [], "else": "$subjects"}}}}
    ])
    if week:
        days = list(days)[7:] if week%2!=0 else list(days)[:7]
    days = [Day(**d) for d in days]
    return days

def create_days(ids):
    for id in ids:
        days_collection.insert_one({'_id': ObjectId(id), 'subjects': []})
    return True

def get_day_by_date(_date: date) -> Day:
    return get_days(_date.isocalendar().week)[_date.weekday()]
