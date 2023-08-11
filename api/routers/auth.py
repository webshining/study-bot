import json

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse, RedirectResponse, Response
from fastapi.templating import Jinja2Templates
from playhouse.shortcuts import model_to_dict

from api.services import generate_tokens
from database.services import get_user
from loader import bot

router = APIRouter()


templates = Jinja2Templates(directory="api/templates")


@router.get('/')
async def login(request: Request):
    bot_username = (await bot.get_me()).username
    return templates.TemplateResponse('login.html', {"bot_username": bot_username, "request": request})

@router.get('/redirect')
async def login_redirect(id: int, redirect: str = None):
    user = get_user(id)
    access_token, refresh_token = generate_tokens({'id': id},{'id': id})
    if redirect:
        response = RedirectResponse(url=redirect + json.dumps({'user': model_to_dict(user), 'accessToken': access_token}))
    else:
        response = JSONResponse({'user': model_to_dict(user), 'accessToken': access_token})
    response.set_cookie('refreshToken', refresh_token)
    return response

@router.get('/logout')
async def logout():
    response = Response(status_code=200)
    response.delete_cookie('refreshToken')
    return response