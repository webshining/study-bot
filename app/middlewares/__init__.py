from loader import dp
from app.middlewares.throttling import ThrottlingMiddleware


if __name__ == 'app.middlewares': 
    dp.setup_middleware(ThrottlingMiddleware())