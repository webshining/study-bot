from aiogram.fsm.state import StatesGroup, State


class List(StatesGroup):
    create_name = State()
    edit_name = State()
    