from pathlib import Path
from aiogram.contrib.middlewares.i18n import I18nMiddleware
from config import I18N_DOMAIN

PATH = f'{Path(__file__).absolute().parent.parent.parent}/locales'

i18n = I18nMiddleware(I18N_DOMAIN, PATH)
