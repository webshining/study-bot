from ..models import User


def get_user(id: int):
    return User.get_or_none(User.id == id)


def get_users(status: str = None):
    if status:
        return list(User.select().where(User.status == status))
    return list(User.select())


def create_user(id: int, name: str, username: str):
    return User.create(id=id, name=name, username=username)


def edit_status(id: int, status: str):
    user = get_user(id)
    user.status = status
    user.save()

    return user


def get_or_create_user(id: int, name: str, username: str):
    user = get_user(id)
    if user:
        user.name = name
        user.username = username
        user.save()
    else:
        user = create_user(id, name, username)

    return user
