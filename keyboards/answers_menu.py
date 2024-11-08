from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def answers_menu_kb():
    kb = [
        [KeyboardButton("Загальнопрофільна підготовка"), KeyboardButton("Вогнева підготовка")],
        [KeyboardButton("Тактична підготовка"), KeyboardButton("Функціональна підготовка")],
        [KeyboardButton("У головне меню")]
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
