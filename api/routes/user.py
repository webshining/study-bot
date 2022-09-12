from fastapi import APIRouter
from database.services import get_users, get_user

router = APIRouter(tags=['User'])


@router.get('')
async def get_users_router(status: str = None):
    users = get_users(status)
    return {'users': [u.dict() for u in users]}


@router.get('/{id}')
async def get_user_router(id: int):
    user = get_user(id)
    return {'user': user.dict()}
