from fastapi import Request
from playhouse.shortcuts import model_to_dict

from database import get_users, edit_status
from . import router


@router.get('/users')
async def all_users_route(status: str = None):
    users = get_users()
    if status:
        users = get_users(status)
    return {"users": [model_to_dict(u) for u in users]}


@router.put('/users/{id}')
async def change_status_route(id: int, body: Request):
    edit_status(id, (await body.json())['status'])
    return {"info": "User status updated!"}
