from fastapi import APIRouter
from playhouse.shortcuts import model_to_dict

from api.services import notfound
from database.services import get_user, get_users

router = APIRouter()

@router.get('/')
async def users():
    return [model_to_dict(u) for u in get_users()]

@router.get('/{id}')
async def user(id: int):
    user = get_user(id)
    return model_to_dict(user) if user else notfound