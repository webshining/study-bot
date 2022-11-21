from ..models import Subject


def get_subjects() -> list[Subject]:
    subjects = Subject.select()
    return list(subjects)


def get_subject(id: int) -> Subject or None:
    subject = Subject.select().where(Subject.id == id).first()
    return subject


def delete_subject(id: int):
    subject = get_subject(id)
    subject.delete_instance()
    return True


def create_subject(name: str, teacher: str, audience: str, info: str = None) -> Subject:
    subject = Subject.create(name=name, teacher=teacher, audience=audience, info=info)
    return subject
