from bson import ObjectId

from ..models import Group, groups_collection
from .users import get_user


def get_groups():
    groups = groups_collection.find()
    groups = [{**g, 'users': [{**get_user(u['_id']), **u} for u in g['users']]} for g in groups]
    return [Group(**g) for g in groups]


def get_group(id: str):
    group = groups_collection.find_one({'_id': ObjectId(id)})
    return group
    