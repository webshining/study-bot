from aiogram.fsm.state import State, StatesGroup


class CreateList(StatesGroup):
    name = State()

class EditList(StatesGroup):
    name = State()
    
class AddToList(StatesGroup):
    text = State()
    