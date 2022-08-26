from bson import ObjectId
from ..models import days_collection, Day


async def init_days():
    if await days_collection.estimated_document_count() != 14:
        days_collection.insert_many([{'subjects': []} for i in range(14)])
    return True


async def get_days(week: int = None):
    days = [d async for d in days_collection.aggregate([
        {'$lookup': {
            'from': 'subjects',
            'localField': 'subjects.subjectId',
            'foreignField': '_id',
            'as': 'subjects'
        }}
    ])]
    if week:
        days = days[:7] if week % 2 != 0 else days[-7:]
    days = [Day(**d) for d in days]
    return days


async def edit_day_subjects(id: str, subjects: list[str]):
    await days_collection.find_one_and_update({'_id': ObjectId(id)}, {'$set': {'subjects': [{'subjectId': ObjectId(s), 'position': i+1} for i, s in enumerate(subjects)]}})
    return True
