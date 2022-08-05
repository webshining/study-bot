from ..models import User


def get_user(id: int):
    return User.get_or_none(id=id)


def create_user(id: int, name: str, username: str):
    return User.create(id=id, name=name, username=username)


def get_or_create_user(id: int, name: str, username: str):
    user = get_user(id)
    if user:
        user.name = name
        user.username = username
        user.save()
    else:
        create_user(id, name, username)

    return user
