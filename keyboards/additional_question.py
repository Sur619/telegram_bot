from aiogram import types


def additional_question_kb():
    return types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="Гендерна рівність"),
             types.KeyboardButton(text="Порядок доступу до персональних даних")],
            [types.KeyboardButton(text="Місцеві вибори"),
             types.KeyboardButton(text="Виборчі правопорушення - як індентифікувати та як реагувати")],
            [types.KeyboardButton(text="Назад↩️")]

        ],
        resize_keyboard=True)


