from ..models import subjects_collection, Subject
from bson.objectid import ObjectId


async def get_subjects():
    subjects = subjects_collection.find()
    return [Subject(**s) async for s in subjects]


async def get_subject(id: str):
    subject = await subjects_collection.find_one({'_id': ObjectId(id)})
    return Subject(**subject) if subject else None


async def create_subject(name: str, audience: str, teacher: str, info: str = None, files: list = None):
    subject = await subjects_collection.insert_one(
        {'name': name, 'audience': audience, 'teacher': teacher, 'info': info, 'files': files})
    return subject


async def update_subject(id: str, name: str, audience: str, teacher: str, info: str, files: list = None):
    subject = await subjects_collection.find_one_and_update({'_id': ObjectId(id)}, {'$set': {'name': name, 'audience': audience, 'teacher': teacher, 'info': info, 'files': files}})
    return subject
