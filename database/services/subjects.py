from ..models import Subject


def get_subject(id: int):
    subject = Subject.get_or_none(id=id)
    return subject


def get_subjects():
    return list(Subject.select())


def add_subject(name: str, audience: str = None, teacher: str = None, info: str = None):
    return Subject.create(name=name, audience=audience, teacher=teacher, info=info)


def delete_subject(id: int):
    subject = get_subject(id)
    if subject:
        subject.delete_instance()
    return True
