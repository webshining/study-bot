def setup_middleware(dp):
    from .user import UserMiddleware
    from .inter import i18n_middleware
    dp.update.middleware(UserMiddleware())
    dp.update.middleware(i18n_middleware)
    