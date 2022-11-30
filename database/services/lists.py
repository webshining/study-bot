from ..models import List, ListElement


def get_list(id: int) -> List:
    list = List.select().where(List.id == id).first()
    return list


def get_lists(all: bool = False) -> list[List]:
    if all:
        lists = List.select()
    else:
        lists = List.select().where(List.visible == True)
    return list(lists)    


def create_list(name: str) -> List:
    list = List.create(name=name)
    return list


def add_entry(key: str, value: str, list_id: int, user_id: int) -> List:
    ListElement.create(key=key, value=value, list_id=list_id, user_id=user_id)
    return get_list(list_id)
