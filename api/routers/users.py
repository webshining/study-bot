from fastapi import APIRouter, Body, Depends
from playhouse.shortcuts import model_to_dict

from api.services import get_current_user, not_enough_rights
from database.models import User
from database.services import get_user, get_users, update_user_status

router = APIRouter()


@router.get('/')
async def users(current_user: User = Depends(get_current_user)):
    return [model_to_dict(u) for u in get_users()]

@router.get('/me')
async def me(current_user: User = Depends(get_current_user)):
    return model_to_dict(current_user)

@router.patch('/{id}')
async def _update_user_status(id: int, 
                              status: str = Body(..., embed=True),
                              current_user: User = Depends(get_current_user)):
    user = get_user(id)
    if status in current_user.statuses_to_edit and user.status in current_user.statuses_to_edit:
        user = update_user_status(id, status)
        return model_to_dict(user)
    else:
        raise not_enough_rights