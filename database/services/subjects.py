from ..models import Subject


def get_subjects() -> list[Subject]:
    subjects = Subject.select()
    return list(subjects)


def get_subject(id: int) -> Subject or None:
    subject = Subject.select().where(Subject.id == id).first()
    return subject


def delete_subject(id: int):
    Subject.delete().where(Subject.id == id).execute()
    return True


def update_subject(id: int, name: str, audience: str, teacher: str, info: str = None):
    subject = Subject(id=id, name=name, audience=audience, teacher=teacher, info=info)
    subject.save()
    return subject


def create_subject(name: str, teacher: str, audience: str, info: str = None) -> Subject:
    subject = Subject.create(name=name, teacher=teacher, audience=audience, info=info)
    return subject
