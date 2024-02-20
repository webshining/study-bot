from aiogram.fsm.state import StatesGroup, State


class GroupState(StatesGroup):
    create = State()
    subject_name = State()
    subject_teacher = State()
    subject_audience = State()
    subject_info = State()
