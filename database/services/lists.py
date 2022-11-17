from bson import ObjectId
from ..models import List, lists_collection


def get_list(id: str):
    _list = lists_collection.find_one({'_id': ObjectId(id)})
    return List(**_list) if _list else None

def create_list(name: str):
    _list = lists_collection.insert_one({'name': name, 'elements': []})
    return get_list(_list.inserted_id)


def get_lists():
    _lists = lists_collection.find()
    return [List(**l) for l in _lists]


def edit_list(id: str, name: str):
    _list = lists_collection.find_one_and_update({'_id': ObjectId(id)}, {'$set': {'name': name}})
    return List(**_list)


def edit_list_elements(id: str, name: str, value: str, user_id: int):
    _list = lists_collection.find_one_and_update({'_id': ObjectId(id)}, {'$push': {'elements': {'name': name, 'value': value, 'user_id': user_id}}})
    return List(**_list)


def delete_list(id: str):
    lists_collection.find_one_and_delete({"_id": ObjectId(id)})
    return True
