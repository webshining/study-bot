from .i18n import i18n


def setup_middlewares(dp):
    dp.middleware.setup(i18n)
