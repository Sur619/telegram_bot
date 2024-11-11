from aiogram import Router, types, F
from keyboards.answers_menu import general_training_kb, answers_menu_kb
import logging
from aiogram.types import CallbackQuery

general_training_router = Router()


# Handler for 'Загальнопрофільна підготовка' button
@general_training_router.message(F.text == 'Загальнопрофільна підготовка')
async def general_training(message: types.Message):
    logging.info(f"User {message.from_user.id} selected 'Загальнопрофільна підготовка'.")
    keyboard = general_training_kb()
    await message.answer('Оберіть опцію:', reply_markup=keyboard)


# Обработчик для кнопок выбора
@general_training_router.message(
    F.text.in_(["Безпека життєдіяльності", "Домедична підготовка", "Психологічна підготовка"]))
async def process_answer(message: types.Message):
    selected_option = message.text
    logging.info(f"User {message.from_user.id} selected '{selected_option}'.")

    # Обновляем клавиатуру с выбранной опцией
    keyboard = general_training_kb(selected_option)
    await message.answer(
        "Введіть запитання або ключові слова🔎\n"
        "Увага! Для швидкого і коректного пошуку введіть запитання повністю.",
        reply_markup=keyboard
    )


# Обработчик для кнопки "Назад"
@general_training_router.message(F.text == 'Назад◀️')
async def go_back(message: types.Message):
    logging.info(f"User {message.from_user.id} selected 'Назад'.")
    # Здесь возвращаем в предыдущее меню
    keyboard = answers_menu_kb()  # Убираем клавиатуру
    await message.answer('Повернення в головне меню', reply_markup=keyboard)
