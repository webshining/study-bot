from fastapi import APIRouter, Depends

from api.models import UserPatch
from api.services import get_current_user, not_enough_rights, notfound
from database.models import User
from database.services import get_user, get_users, update_user_status

router = APIRouter(dependencies=[Depends(get_current_user)])


@router.get('/')
async def users():
    users = get_users()
    return [u.to_dict() for u in users]


@router.get('/{id}')
async def user(id: int):
    user = get_user(id)
    return user.to_dict() if user else notfound


@router.patch('/{id}')
async def user(id: int, dto: UserPatch, current_user: User = Depends(get_current_user)):
    user = update_user_status(id, dto.status)
    statuses_to_edit = current_user.statuses_to_edit
    if user and dto.status not in statuses_to_edit or user.status not in statuses_to_edit:
        return not_enough_rights
    return user.to_dict() if user else notfound
