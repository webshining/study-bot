def setup_middleware(dp):
    from .user import UserMiddleware
    from .inter import i18n
    dp.setup_middleware(UserMiddleware())
    dp.setup_middleware(i18n)
