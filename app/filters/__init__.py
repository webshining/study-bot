from .status import StatusFilter
from loader import dp

if __name__ == 'app.filters':
    dp.filters_factory.bind(StatusFilter)
