from ..models import User, users_collection


def get_users():
    users = users_collection.find()
    return [User(**u) for u in users]


def get_user(id: int):
    user = users_collection.find_one({'_id': id})
    return User(**user)