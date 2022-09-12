from ..models import User, users_collection


def get_users(status: str = None):
    users = users_collection.find({'status': status}) if status else users_collection.find({'status': status})
    return [User(**u) for u in users]


def get_user(id: int):
    user = users_collection.find_one({'_id': id})
    return User(**user) if user else None


def create_user(id: int, name: str, username: str):
    user = users_collection.insert_one({'_id': id, 'name': name, 'username': username, 'status': 'user'})
    return get_user(user.inserted_id)
