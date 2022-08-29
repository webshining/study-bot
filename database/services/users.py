from ..models import users_collection, User


async def get_user(id: int):
    user = await users_collection.find_one({'_id': id})
    return User(**user) if user else None


async def get_users():
    users = users_collection.find()
    return [User(**u) async for u in users]


async def create_user(id: int, name: str, username: str):
    return await users_collection.insert_one({'_id': id, 'name': name, 'username': username, 'status': 'user'})


async def update_user_status(id: int, status: str):
    return await users_collection.find_one_and_update({'_id': id}, {'$set': {'status': status}})


async def get_or_create_user(id: int, name: str, username: str):
    user = await get_user(id)
    if user:
        await users_collection.find_one_and_update({'_id': id}, {'$set': {'name': name, 'username': username}})
    else:
        await create_user(id, name, username)
    return await get_user(id)
