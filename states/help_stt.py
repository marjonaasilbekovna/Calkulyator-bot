from aiogram.fsm.state import State, StatesGroup

class Help(StatesGroup):
    help = State()

class Eslatma(StatesGroup):
    nomi = State()
    eslatma = State()
