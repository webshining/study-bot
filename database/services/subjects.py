from bson import ObjectId
from ..models import Subject, subjects_collection


def get_subjects():
    return [Subject(**s) for s in subjects_collection.find()]


def get_subject(id: str):
    subject = subjects_collection.find_one({'_id': ObjectId(id)})
    return Subject(**subject) if subject else None


def create_subject(name: str, teacher: str, audience: str = None, info: str = None):
    subject = subjects_collection.insert_one({"name": name, "audience": audience, 'teacher': teacher, 'info': info})
    return get_subject(subject.inserted_id)
