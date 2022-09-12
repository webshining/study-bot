from fastapi import APIRouter

from api.dto import SubjectDTO
from database.services import get_subjects, get_subject, create_subject

router = APIRouter(tags=['Subject'])


@router.get('')
async def get_subjects_router():
    subjects = get_subjects()
    return {'subjects': [s.dict() for s in subjects]}


@router.get('/{id}')
async def get_subject_router(id: str):
    subject = get_subject(id)
    return {'subject': subject.dict()}


@router.post('')
async def create_subject_router(subject: SubjectDTO):
    subject = create_subject(*subject.dict().values())
    return {'subject': subject.dict()}
