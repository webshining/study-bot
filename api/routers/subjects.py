from fastapi import APIRouter
from playhouse.shortcuts import model_to_dict

from api.models import SubjectPatch
from api.services import notfound
from database.services import get_subject, get_subjects, update_subject

router = APIRouter()

@router.get('/')
async def subjects():
    return [model_to_dict(s) for s in get_subjects()]

@router.get('/{id}')
async def subject(id: int):
    subject = get_subject(id)
    return model_to_dict(subject) if subject else notfound

@router.patch('/{id}')
async def edit_subject(id: int, dto: SubjectPatch):
    subject = update_subject(id, dto.name, dto.audience, dto.teacher, dto.info)
    return model_to_dict(subject) if subject else notfound