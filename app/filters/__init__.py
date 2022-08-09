from loader import dp
from .status import Status

if __name__ == 'app.filters':
    dp.filters_factory.bind(Status)
