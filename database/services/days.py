from bson import ObjectId

from ..models import days_collection


async def init_days():
    if len(list(await days_collection.find().to_list(length=100))) != 14:
        days_collection.insert_many([{'subjects': []} for i in range(14)])
    return True


async def get_days(week: int = None):
    days = await days_collection.find().to_list(length=100)
    if week:
        days = list(await days_collection.find().to_list(length=100))[:7] if week % 2 != 0 else list(await days_collection.find().to_list(length=100))[-7:]
    return days


async def update_day_subjects(id: str, subjects: list[str]):
    await days_collection.find_one_and_update({'_id': ObjectId(id)}, {'$set': {'subjects': [ObjectId(s) for s in subjects]}})
    return True
