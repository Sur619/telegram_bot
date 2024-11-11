from aiogram import types

from keyboards.rules_menu import rules_menu_kb


async def in_development(message: types.Message, text: str = "Функція в розробці.", keyboard=None) -> None:
    """Функция-заглушка для ответов с удалением клавиатуры."""
    if keyboard is None:
        keyboard = types.ReplyKeyboardRemove()  # Убираем клавиатуру, если не передана
    await message.answer(text, reply_markup=keyboard)