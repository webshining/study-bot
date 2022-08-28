from ..models import subjects_collection, Subject
from bson.objectid import ObjectId


async def get_subjects():
    subjects = subjects_collection.find()
    return [Subject(**s) async for s in subjects]


async def get_subject(id: str):
    subject = await subjects_collection.find_one({'_id': ObjectId(id)})
    return Subject(**subject)


async def create_subject(name: str, audience: str, teacher: str, info: str = ''):
    subject = await subjects_collection.insert_one(
        {'name': name, 'audience': audience, 'teacher': teacher, 'info': info})
    return subject


async def update_subject(id: str, name: str, audience: str, teacher: str, info: str):
    subject = await subjects_collection.find_one_and_update({'_id': ObjectId(id)}, {'$set': {'name': name, 'audience': audience, 'teacher': teacher, 'info': info}})
    return subject
