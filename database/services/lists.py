from ..models import List, ListElement


def get_list(id: int) -> List or None:
    list = List.select().where(List.id == id).first()
    return list


def get_lists() -> list[List]:
    lists = List.select()
    return list(lists)    


def create_list(name: str) -> List:
    list = List.create(name=name)
    return list


def add_entry(key: str, value: str, list_id: int) -> List:
    ListElement.create(key=key, value=value, list_id=list_id)
    return get_list(list_id)
