from transliterate import translit
from ..models import subjects


def get_subject(codename: str):
    _subject = subjects.find_one({'codename': codename})
    return _subject


def get_subjects():
    _subjects = subjects.find()
    return _subjects


def create_subject(name: str, audience: str, teacher: str, info: str = ''):
    try:
        codename = translit(name, reversed=True).lower()
    except:
        codename = name.lower()
    _subject = subjects.insert_one({'codename': codename, 'name': name, 'audience': audience, 'teacher': teacher, 'info': info})
    return _subject


def delete_subject():
    subjects.find_one_and_delete({''})
