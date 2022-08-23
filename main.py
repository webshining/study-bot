from venv import create
from aiogram import executor


if __name__ == '__main__':
    from database import get_user, get_or_create_user
    print(get_or_create_user(35645674, 'aboba', 'amogus'))
