from loader import dp
from .admin import AdminFilter

if __name__ == '__main__':
    dp.filters_factory.bind(AdminFilter)