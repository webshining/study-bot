from ..models import Chat


def get_or_create_chat(chat_id: int) -> Chat:
    chat: Chat = Chat.get_or_none(Chat.chat_id == chat_id)
    if not chat:
        chat = Chat.create(chat_id=chat_id)
    return chat


def update_chat(chat_id: int, group_id: int) -> Chat:
    chat: Chat = Chat.get_or_none(Chat.chat_id == chat_id)
    chat.group_id = group_id
    chat.save()
    return chat
