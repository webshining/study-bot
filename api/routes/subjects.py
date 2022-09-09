from api import subjectsRouter
from pydantic import BaseModel
from database import get_subjects, get_subject, File, create_subject


class Subject(BaseModel):
    name: str
    audience: str
    teacher: str
    info: str = None
    files: list[File] = None


@subjectsRouter.get('/subjects')
async def get_all_subjects_router(limit: int = None):
    subjects = await get_subjects()
    return {'subjects': [s.dict() for s in (subjects[:limit] if limit else subjects)]}


@subjectsRouter.get('/subjects/{id}')
async def get_one_subject_router(id: str):
    try:
        subject = await get_subject(id)
        return {'subject': subject.dict()} if subject else {'error': 'Subject not found!'}
    except:
        return {'error': "Not correct id!"}


@subjectsRouter.post('/subjects')
async def create_subject_router(subject: Subject):
    await create_subject(subject.name, subject.audience, subject.teacher, subject.info, subject.files)
    return {'info': 'Subject created!'}
