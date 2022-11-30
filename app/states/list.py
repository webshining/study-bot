from aiogram.fsm.state import StatesGroup, State


class ListStates(StatesGroup):
    create_name = State()
    edit_name = State()
    write = State()
    