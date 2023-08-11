from datetime import datetime, timedelta
from typing import NamedTuple

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2AuthorizationCodeBearer

from data.config import (ACCESS_SECRET_KEY, ACCESS_TOKEN_EXPIRE_MINUTES,
                         REFRESH_SECRET_KEY, REFRESH_TOKEN_EXPIRE_MINUTES)
from database.services import get_user

oauth2_scheme = OAuth2AuthorizationCodeBearer(tokenUrl='/api/auth/redirect', authorizationUrl='/api/auth' )


class Tokens(NamedTuple):
    access_token: str
    refresh_token: str
    
def generate_tokens(access_data: dict, refresh_data: dict) -> Tokens:
    access_data['exp'] = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    refresh_data['exp'] = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    
    access_token = jwt.encode(access_data, ACCESS_SECRET_KEY, algorithm='HS256')
    refresh_token = jwt.encode(refresh_data, REFRESH_SECRET_KEY, algorithm='HS256')
    return Tokens(access_token=access_token, refresh_token=refresh_token)

def get_current_user(token: str = Depends(oauth2_scheme), refresh: bool = False):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not validate credentials',
    )
    try:
        payload = jwt.decode(token, REFRESH_SECRET_KEY if refresh else ACCESS_SECRET_KEY, algorithms=['HS256'])
        user = get_user(int(payload['id']))
        if not user or user.status not in ("admin", "super_admin"):
            raise credentials_exception
        return user
    except:
        raise credentials_exception
    