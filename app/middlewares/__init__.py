from .i18n import i18n
from .logging import LoggingMiddleware


def setup_middlewares(dp):
    dp.middleware.setup(i18n)
    dp.middleware.setup(LoggingMiddleware())
