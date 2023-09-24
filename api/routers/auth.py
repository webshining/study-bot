import json

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from api.services import (delete_token, generate_tokens, get_current_user,
                          is_telegram, unauthorized)
from data.config import REFRESH_TOKEN_EXPIRE_MINUTES
from database.services import get_user
from loader import bot

router = APIRouter()

templates = Jinja2Templates(directory="api/templates")


@router.get('/')
async def login(request: Request, redirect: str = ""):
    bot_username = (await bot.get_me()).username
    return templates.TemplateResponse('login.html', {"bot_username": bot_username,
                                                     "redirect": request.url_for('login_redirect').include_query_params(
                                                         redirect=redirect), "request": request})


@router.get('/redirect')
async def login_redirect(id: int, redirect: str, request: Request):
    if is_telegram(dict(request.query_params)):
        user = get_user(id)
        if not user:
            return unauthorized
        access_token, refresh_token = await generate_tokens({'id': id}, {'id': id})
        data = {"user": user.to_dict(), "accessToken": access_token}
        if redirect:
            response = RedirectResponse(f'{redirect}#{json.dumps(data)}')
        else:
            response = JSONResponse(data)
        response.set_cookie(key='refreshToken', value=refresh_token, max_age=REFRESH_TOKEN_EXPIRE_MINUTES * 60,
                            httponly=True, samesite='none')
        return response
    else:
        return unauthorized


@router.get('/refresh')
async def refresh(request: Request):
    refresh_token = request.cookies.get('refreshToken')
    if not refresh_token:
        raise unauthorized
    user = await get_current_user(refresh_token, True)
    await delete_token(refresh_token)
    access_token, refresh_token = await generate_tokens({'id': user.id}, {'id': user.id})
    response = JSONResponse({'user': user.to_dict(), 'accessToken': access_token})
    response.set_cookie(key='refreshToken', value=refresh_token, httponly=True,
                        max_age=REFRESH_TOKEN_EXPIRE_MINUTES * 60, samesite='none')
    return response


@router.get('/logout')
async def logout():
    response = JSONResponse({'ok': True})
    response.delete_cookie(key='refreshToken', secure=True, httponly=True, samesite='none')
    return response
