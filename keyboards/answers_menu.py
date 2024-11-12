from aiogram import types


def answers_menu_kb():
    return types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Загальнопрофільна підготовка"),
                types.KeyboardButton(text="Вогнева підготовка")
            ],
            [
                types.KeyboardButton(text="Тактична підготовка"),
                types.KeyboardButton(text="Функціональна підготовка")
            ],
            [
                types.KeyboardButton(text="Додаткові заняття")
            ],
            [
                types.KeyboardButton(text="У головне меню↩️")
            ]
        ],
        resize_keyboard=True
    )


def general_training_kb(selected_option=None):
    return types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="📌Безпека життєдіяльності📌" if selected_option == "Безпека життєдіяльності" else "Безпека життєдіяльності")],
            [types.KeyboardButton(text="📌Домедична підготовка📌" if selected_option == "Домедична підготовка" else "Домедична підготовка")],
            [types.KeyboardButton(text="📌Психологічна підготовка📌" if selected_option == "Психологічна підготовка" else "Психологічна підготовка")],
            [types.KeyboardButton(text="Назад◀️")]
        ],
        resize_keyboard=True
    )