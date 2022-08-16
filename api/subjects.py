from playhouse.shortcuts import model_to_dict
from pydantic import BaseModel

from . import router
from database import get_subjects, get_subject, edit_subject, delete_subject, create_subject


class SubjectType(BaseModel):
    name: str
    audience: str
    teacher: str
    info: str


@router.get('/subjects')
async def all_subjects_route():
    return {"subjects": [model_to_dict(s) for s in get_subjects()]}


@router.post('/subjects')
async def all_subjects_route(subject: SubjectType):
    create_subject(*subject.dict().values())
    return {"info": "Subject created!"}


@router.get('/subjects/{id}')
async def edit_subject_route(id: int):
    return {"subject": model_to_dict(get_subject(id))}


@router.put('/subjects/{id}')
async def edit_subject_route(id: int, subject: SubjectType):
    edit_subject(id, *subject.dict().values())
    return {"info": "Subject edited!"}


@router.delete('/subjects/{id}')
async def edit_subject_route(id: int):
    delete_subject(id)
    return {"info": "Subject deleted!"}
