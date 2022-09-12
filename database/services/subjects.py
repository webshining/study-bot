from bson import ObjectId
from ..models import Subject, File, subjects_collection


def get_subjects():
    return [Subject(**s) for s in subjects_collection.find()]


def get_subject(id: str):
    subject = subjects_collection.find_one({'_id': ObjectId(id)})
    return Subject(**subject) if subject else None


def create_subject(name: str, audience: str, teacher: str, info: str, files: list[File]):
    subject = subjects_collection.insert_one({"name": name, "audience": audience, 'teacher': teacher, 'info': info, 'files': files})
    return get_subject(subject.inserted_id)
