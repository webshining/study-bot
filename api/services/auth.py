import hashlib
import hmac
from datetime import datetime, timedelta
from typing import NamedTuple

import jwt
from fastapi import Depends
from fastapi.security import OAuth2AuthorizationCodeBearer

from data.config import (ACCESS_SECRET_KEY, ACCESS_TOKEN_EXPIRE_MINUTES,
                         REFRESH_SECRET_KEY, REFRESH_TOKEN_EXPIRE_MINUTES,
                         TELEGRAM_BOT_TOKEN)
from database.services import get_user
from loader import redis

from .exceptions import unauthorized, not_enough_rights

oauth2_scheme = OAuth2AuthorizationCodeBearer(tokenUrl='/api/auth/redirect', authorizationUrl='/api/auth')


class Tokens(NamedTuple):
    access_token: str
    refresh_token: str


async def generate_tokens(access_data: dict, refresh_data: dict) -> Tokens:
    access_data['exp'] = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    refresh_data['exp'] = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)

    access_token = jwt.encode(access_data, ACCESS_SECRET_KEY, algorithm='HS256')
    refresh_token = jwt.encode(refresh_data, REFRESH_SECRET_KEY, algorithm='HS256')
    await save_token(refresh_token, REFRESH_TOKEN_EXPIRE_MINUTES * 60)

    return Tokens(access_token=access_token, refresh_token=refresh_token)


async def get_current_user(token: str = Depends(oauth2_scheme), refresh: bool = False):
    try:
        payload = jwt.decode(token, REFRESH_SECRET_KEY if refresh else ACCESS_SECRET_KEY, algorithms=['HS256'])
        user = get_user(int(payload['id']))
        if not user:
            await delete_token(token)
            raise unauthorized
        elif user.status not in ("admin", "super_admin"):
            await delete_token(token)
            raise not_enough_rights
        return user
    except:
        await delete_token(token)
        raise unauthorized


def is_telegram(data: dict) -> bool:
    try:
        hash = data['hash']
        del data['redirect']
        del data['hash']
        sorted_data = dict(sorted(data.items()))
        data_check_string = '\n'.join('='.join(i) for i in sorted_data.items()).encode()
        secret_key = hashlib.sha256(TELEGRAM_BOT_TOKEN.encode()).digest()
        return hmac.new(secret_key, data_check_string, hashlib.sha256).hexdigest() == hash
    except:
        return False


async def save_token(token: str, ex: int):
    await redis.set(token, 'token', ex=ex)


async def delete_token(token: str):
    await redis.delete(token)
