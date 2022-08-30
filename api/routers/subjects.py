from .. import subjectsRouter
from database import get_subjects, get_subject, create_subject, update_subject
from ..models import Subject


@subjectsRouter.get('/')
async def get_subjects_router():
    subjects = [s.dict() for s in await get_subjects()]
    return {'subjects': subjects}


@subjectsRouter.get('/{id}')
async def get_subject_router(id: str):
    subject = await get_subject(id)
    return {'subject': subject.dict() if subject else None}


@subjectsRouter.put('/{id}')
async def update_subject_router(id: str, subject: Subject):
    await update_subject(id, *subject.dict().values())
    return {'info': 'Subject updated!'}


@subjectsRouter.post('/')
async def create_subject_router(subject: Subject):
    await create_subject(*subject.dict().values())
    return {'info': 'Subject created!'}
