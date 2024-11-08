from aiogram import Router, types
from keyboards.answers_menu import answers_menu_kb
import logging

answers_router = Router()


@answers_router.message(lambda message: message.text == "Пошук Відповідей")
async def answers_menu(message: types.Message):
    logging.info(f"User {message.from_user.id} selected 'Пошук Відповідей'.")
    await message.answer("Оберіть опцію:", reply_markup=answers_menu_kb())


@answers_router.message(
    lambda message: message.text in ["Безпека життєдіяльності", "Домедична підготовка", "Психологічна підготовка"])
async def process_answer(message: types.Message):
    await message.answer("Введіть запитання або ключові слова🔎\nУвага! Введіть запитання повністю.")
