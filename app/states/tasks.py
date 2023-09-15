from aiogram.fsm.state import StatesGroup, State


class CreateTaskState(StatesGroup):
    name = State()
    text = State()
    files = State()
    date = State()
