from bson import ObjectId
from ..models import Subject, subjects_collection, days_collection


def get_subjects() -> list[Subject]:
    return [Subject(**s) for s in subjects_collection.find()]


def get_subject(id: str) -> Subject or None:
    subject = subjects_collection.find_one({'_id': ObjectId(id)})
    return Subject(**subject) if subject else None


def create_subject(name: str, teacher: str, audience: str, info: str) -> Subject:
    subject = subjects_collection.insert_one({"name": name, "audience": audience, 'teacher': teacher, 'info': info})
    return get_subject(subject.inserted_id)


def edit_subject(id: str, **kwargs):
    subject = subjects_collection.find_one_and_update({'_id': ObjectId(id)}, {'$set': kwargs}, return_document=True)
    return Subject(**subject)


def delete_subject(id: str):
    subjects_collection.find_one_and_delete({'_id': ObjectId(id)})
    days_collection.update_many({}, {"$pull": {"subjects": {"_id": {"$eq": id}}}})
    return True
