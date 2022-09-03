from aiogram.contrib.middlewares.i18n import I18nMiddleware
from data.config import DIR, I18N_DOMAIN

i18n = I18nMiddleware(I18N_DOMAIN, f'{DIR}/data/locales')
