import json

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from api.services import (delete_token, generate_tokens, get_current_user,
                          is_telegram, not_enough_rights, unauthorized)
from data.config import FRONTEND_URL, REFRESH_TOKEN_EXPIRE_MINUTES
from database.services import get_user
from loader import bot

router = APIRouter()

templates = Jinja2Templates(directory="api/templates")


@router.get('/')
async def login(request: Request, status: str = FRONTEND_URL):
    bot_username = (await bot.get_me()).username
    return templates.TemplateResponse('login.html', {"bot_username": bot_username,
                                                     "redirect": request.url_for('login_redirect').include_query_params(
                                                         status=status), "request": request})


@router.get('/redirect')
async def login_redirect(id: int, request: Request, status: str = FRONTEND_URL):
    if is_telegram(dict(request.query_params)):
        user = get_user(id)
        if not user:
            return RedirectResponse(f'{status}#{json.dumps({"detail": unauthorized.detail})}')
        if user.status not in ("admin", "super_admin"):
            return RedirectResponse(f'{status}#{json.dumps({"detail": not_enough_rights.detail})}')
        access_token, refresh_token = await generate_tokens({'id': id}, {'id': id})
        data = {"user": user.to_dict(), "accessToken": access_token}
        response = RedirectResponse(f'{status}#{json.dumps(data)}')
        response.set_cookie(key='refreshToken', value=refresh_token, max_age=REFRESH_TOKEN_EXPIRE_MINUTES * 60,
                            httponly=True, samesite='none', secure=True)
        return response
    else:
        return RedirectResponse(f'{status}#{json.dumps({"detail": unauthorized.detail})}')


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
                        max_age=REFRESH_TOKEN_EXPIRE_MINUTES * 60, samesite='none', secure=True)
    return response


@router.get('/logout')
async def logout():
    response = JSONResponse({'message': "ok"})
    response.delete_cookie(key='refreshToken', secure=True, httponly=True, samesite='none')
    return response
