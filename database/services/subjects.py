from ..models import Subject


def get_subject(id: int):
    return Subject.get_or_none(id=id)


def get_subjects():
    return list(Subject.select())


def create_subject(name: str, audience: str, teacher: str, info: str):
    return Subject.create(name=name, audience=audience, teacher=teacher, info=info)


def delete_subject(id: int):
    subject = get_subject(id)
    if subject:
        subject.delete_instance()
    return True
