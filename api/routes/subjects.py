from fastapi import APIRouter

from database.models import Subject
from database.services import get_subject, get_subjects, create_subject, edit_subject, delete_subject

router = APIRouter(prefix='/subjects')


@router.get('/')
async def _subjects_get():
    subjects = get_subjects()
    return {'subjects': subjects}


@router.get('/{id}')
async def _subject_get(id: str):
    subject = get_subject(id)
    return {'subject': subject}


@router.put('/{id}')
async def _subject_put(id: str, subject: Subject):
    subject = edit_subject(id, name=subject.name, teacher=subject.teacher, audience=subject.audience, info=subject.info, files=subject.files)
    return {'subject': subject}


@router.post('/')
async def _subject_post(subject: Subject):
    subject = create_subject(name=subject.name, teacher=subject.teacher, audience=subject.audience, info=subject.info)
    return {'subject': subject}


@router.delete('/{id}')
async def _subject_delete(id: str):
    delete_subject(id)
    return {'message': "Subject has been removed"}
