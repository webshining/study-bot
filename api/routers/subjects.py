from fastapi import APIRouter, Depends

from api.models import SubjectCreate, SubjectPatch
from api.services import get_current_user, notfound
from database.services import (create_subject, delete_subject, get_subject,
                               get_subjects, update_subject)

router = APIRouter(dependencies=[Depends(get_current_user)])


@router.get('/')
async def _subjects():
    subjects = get_subjects()
    return [s.to_dict() for s in subjects]


@router.get('/{id}')
async def _subject(id: int):
    subject = get_subject(id)
    return subject.to_dict() if subject else notfound


@router.patch('/{id}')
async def _edit_subject(id: int, dto: SubjectPatch):
    subject = update_subject(id, dto.name, dto.audience, dto.teacher, dto.info)
    return subject.to_dict() if subject else notfound


@router.post('/')
async def _create_subject(dto: SubjectCreate):
    subject = create_subject(name=dto.name, teacher=dto.teacher, audience=dto.audience, info=dto.info)
    return subject.to_dict()


@router.delete('/{id}')
async def _delete_subject(id: int):
    delete_subject(id)
    return {"message": "Success"}
