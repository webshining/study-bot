from .. import usersRouter
from database import get_users


@usersRouter.get('/')
async def get_all_users_router():
    return {'users': [u.dict() for u in await get_users()]}
