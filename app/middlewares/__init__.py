def setup_middlewares(dp):
    from .i18n import i18n

    dp.middleware.setup(i18n)
