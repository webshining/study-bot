from ..models import User


def get_users() -> list[User]:
    users = User.select()
    return list(users)


def get_user(id: int) -> User or None:
    user = User.select().where(User.id == id).first()
    return user


def create_user(id: int, name: str, username: str = None) -> User:
    user = User.create(id=id, name=name, username=username)
    return user


def update_user(id: int, name: str, username: str = None) -> User:
    user = User(id=id, name=name, username=username)
    user.save()
    return user


def update_user_status(id: int, status: str) -> User | None:
    user = User(id=id, status=status)
    user.save()
    return user


def get_or_create_user(id: int, name: str, username: str = None) -> User:
    user = get_user(id)
    if user:
        user = update_user(id, name, username)
    else:
        user = create_user(id, name, username)
    return user
