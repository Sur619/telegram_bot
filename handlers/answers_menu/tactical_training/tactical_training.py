from aiogram import Router, types, F

from handlers.in_development import in_development
from keyboards.answers_menu import answers_menu_kb
import logging
from aiogram.types import CallbackQuery

tactical_training_router = Router()


# Handler for 'Загальнопрофільна підготовка' button
@tactical_training_router.message(F.text == 'Функціональна підготовка')
async def tactical_training(message: types.Message):
    logging.info(f"User {message.from_user.id} selected 'Вогнева підготовка'.")
    keyboard = answers_menu_kb()
    await in_development(message, keyboard=keyboard)
#
# # Обработчик для кнопок выбора
# @general_training_router.message(
#     F.text.in_(["Безпека життєдіяльності", "Домедична підготовка", "Психологічна підготовка"]))
# async def process_answer(message: types.Message):
#     selected_option = message.text
#     logging.info(f"User {message.from_user.id} selected '{selected_option}'.")
#
#     # Обновляем клавиатуру с выбранной опцией
#     keyboard = general_training_kb(selected_option)
#     await message.answer(
#         "Введіть запитання або ключові слова🔎\n"
#         "Увага! Для швидкого і коректного пошуку введіть запитання повністю.",
#         reply_markup=keyboard
#     )
#
#
# # Обработчик для кнопки "Назад"
# @general_training_router.message(F.text == 'Назад◀️')
# async def go_back(message: types.Message):
#     logging.info(f"User {message.from_user.id} selected 'Назад'.")
#     # Здесь возвращаем в предыдущее меню
#     keyboard = answers_menu_kb()  # Убираем клавиатуру
#     await message.answer('Повернення в головне меню', reply_markup=keyboard)
