from ..models import User


def get_users(chat_id: int = None) -> list[User]:
    users = User.select()
    if chat_id:
        users = users.where(User.chat_id == chat_id)
    return list(User.select())

def get_or_create_user(name: str, user_id: int, chat_id: int) -> User:
    user: User = User.get_or_none((User.user_id == user_id) & (User.chat_id == chat_id))
    if user:
        user.name = name
        user.save()
    else:
        user = User.create(name=name, user_id=user_id, chat_id=chat_id)
    return user
    