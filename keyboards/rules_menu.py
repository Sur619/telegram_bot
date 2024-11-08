from aiogram import types


def rules_menu_kb():
    return types.ReplyKeyboardMarkup(
        keyboard=
        [
            [types.KeyboardButton(text="Найчастіші запитання❓")],
            [types.KeyboardButton(text="Повідомити про помилку🖍")],
            [types.KeyboardButton(text="У головне меню↩️")]
        ],
        resize_keyboard=True)
