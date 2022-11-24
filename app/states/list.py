from aiogram.fsm.state import StatesGroup, State


class ListCreate(StatesGroup):
    name = State()
    