from ..models import User


def get_users() -> list[User]:
    users = User.select().order_by(User.id)
    return list(users)

def get_or_create_user(name: str, user_id: int, username: str = None) -> User:
    user: User = User.get_or_none(User.user_id == user_id)
    if user:
        user.name = name
        user.username = username
        user.save()
    else:
        user = User.create(name=name, user_id=user_id)
    return user