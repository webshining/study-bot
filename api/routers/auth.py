from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from loader import bot

router = APIRouter()


templates = Jinja2Templates(directory="api/templates")


@router.get('/')
async def login(request: Request):
    bot_username = (await bot.get_me()).username
    return templates.TemplateResponse('login.html', {"bot_username": bot_username, "request": request})


@router.get('/redirect')
async def login_redirect(request: Request):
    return request.query_params