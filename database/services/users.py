from ..models import users


def get_user(id: int):
    _user = users.find_one({'user_id': id})
    return _user


def get_users(status: str = None):
    _users = users.find({'status': status}) if status else users.find()
    return _users


def create_user(id: int, name: str, username: str, status: str = 'user'):
    _user = users.insert_one({'user_id': id, 'name': name, 'username': username, 'status': status})
    return _user


def get_or_create_user(id: int, name: str, username: str):
    _user = get_user(id)
    if _user:
        _user = users.find_one_and_update({'user_id': id}, {'$set': {'name': name, 'username': username}})
    else:
        _user = create_user(id, name, username)
        
    return _user
