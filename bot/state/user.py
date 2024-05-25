from aiogram.fsm.state import StatesGroup, State


class UserState(StatesGroup):
    choice_work = State()
    wait_file = State()