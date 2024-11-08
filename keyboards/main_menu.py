from aiogram import types


def main_menu_kb():
    return types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Тестування"),
                types.KeyboardButton(text="Пошук Відповідей")
            ],
            [
                types.KeyboardButton(text="Термін дії моєї підписки"),
                types.KeyboardButton(text="Придбати VIP доступ")
            ],
            [types.KeyboardButton(text="Правила користування")]
        ],
        resize_keyboard=True
    )
