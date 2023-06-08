from ..models import User


def get_users(chat_id: int) -> list[User]:
    return list(User.select().where(User.chat_id == chat_id))

def get_or_create_user(name: str, user_id: int, chat_id: int) -> User:
    user: User = User.get_or_none((User.user_id == user_id) & (User.chat_id == chat_id))
    if user:
        user.name = name
        user.save()
    else:
        user = User.create(name=name, user_id=user_id, chat_id=chat_id)
    return user