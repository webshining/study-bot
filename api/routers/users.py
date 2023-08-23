from fastapi import APIRouter, Body, Depends
from playhouse.shortcuts import model_to_dict

from api.services import get_current_user, notfound
from database.services import get_user, get_users, update_user_status

router = APIRouter(dependencies=[Depends(get_current_user)])

@router.get('/')
async def users():
    return [model_to_dict(u) for u in get_users()]

@router.get('/{id}')
async def user(id: int):
    user = get_user(id)
    return model_to_dict(user) if user else notfound

@router.patch('/{id}')
async def user(id: int, status: str = Body(..., embed=True)):
    user = update_user_status(id, status)
    return model_to_dict(user) if user else notfound