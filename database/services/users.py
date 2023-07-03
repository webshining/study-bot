from bson import ObjectId

from ..models import User, users_collection


def get_users() -> list[User]:
    return [User(**s) for s in users_collection.find()]


def get_user(user_id: int) -> User or None:
    user = users_collection.find_one({'user_id': user_id})
    return User(**user) if user else None


def create_user(user_id: int, name: str, username: str = None) -> User:
    users_collection.insert_one({"user_id": user_id, "name": name, "username": username, "status": "user"})
    return get_user(user_id)


def edit_user(user_id: int, **kwargs) -> User:
    user = users_collection.find_one_and_update({'user_id': user_id}, {'$set': kwargs}, return_document=True)
    return User(**user)

def get_or_create_user(user_id: int, name: str, username: str = None) -> User:
    user = get_user(user_id)
    if not user:
        user = create_user(user_id=user_id, name=name, username=username)
    if user:
        user = edit_user(user_id, username=username, name=name)
    return user
