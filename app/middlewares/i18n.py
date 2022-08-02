from pathlib import Path
from aiogram.contrib.middlewares.i18n import I18nMiddleware
from data.config import I18N_DOMAIN

i18n = I18nMiddleware(I18N_DOMAIN, f'{Path(__file__).absolute().parent.parent.parent}/data/locales')
