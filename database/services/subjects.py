from ..models import Subject


def create_subject(name: str, audience: str, teacher: str, info: str):
    return Subject.create(name=name, audience=audience, teacher=teacher, info=info)


def get_subject(id: int):
    return Subject.get_or_none(Subject.id == id)


def get_subjects():
    subjects = list(Subject.select())
    return subjects


def delete_subject(id: int):
    subject = get_subject(id)
    subject.delete_instance()
    return True


def edit_subject(id: int, name: str, audience: str, teacher: str, info: str):
    subject = get_subject(id)
    subject.name = name
    subject.audience = audience
    subject.teacher = teacher
    subject.info = info
    subject.save()
    return subject
