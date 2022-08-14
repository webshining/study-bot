from ..models import Subject


def get_subject(id: int):
    return Subject.get_by_id(id)


def get_subjects():
    return list(Subject.select())
