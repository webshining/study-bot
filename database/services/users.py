from ..models import User


def get_user(id: int):
    user = User.get_or_none(User.id == id)
    return user


def create_user(id: int, name: str, username: str):
    user = User.create(id, name, username)
    return user


def update_user(id: int, name: str, username: str):
    user = get_user(id)
    user.name = name
    user.username = username
    user.save()
    return user


def get_or_create_user(id: int, name: str, username: str):
    user = get_user(id)
    if user:
        user = update_user(id, name, username)
    else:
        user = create_user(id, name, username)

    return user
