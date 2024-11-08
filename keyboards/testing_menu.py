from aiogram import types


def testing_menu_kb():
    return types.ReplyKeyboardMarkup(keyboard=
    [
        [types.KeyboardButton(text='Види тестування')],
        [types.KeyboardButton(text='У головне меню↩️')]]
        , resize_keyboard=True
    )
