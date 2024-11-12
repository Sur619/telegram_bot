import logging

from aiogram import Router, F, types
from aiogram.types import Message

from handlers.in_development import in_development
from keyboards import main_menu_kb, answers_menu_kb
from keyboards.additional_question import additional_question_kb

additional_question_router = Router()


@additional_question_router.message(F.text == "Додаткові заняття")
async def additional_question(message: Message):
    keyboard = additional_question_kb()
    await message.answer("Додаткові заняття", reply_markup=keyboard)


@additional_question_router.message(F.text == "Порядок доступу до персональних даних")
async def additional_question(message: Message):
    keyboard = additional_question_kb()
    await in_development(message, keyboard=keyboard)


@additional_question_router.message(F.text == "Гендерна рівність")
async def additional_question(message: Message):
    keyboard = additional_question_kb()
    await in_development(message, keyboard=keyboard)


@additional_question_router.message(F.text == "Місцеві вибори")
async def additional_question(message: Message):
    keyboard = additional_question_kb()
    await in_development(message, keyboard=keyboard)


@additional_question_router.message(F.text == "Виборчі правопорушення - як індентифікувати та як реагувати")
async def additional_question(message: Message):
    keyboard = additional_question_kb()
    await in_development(message, keyboard=keyboard)


@additional_question_router.message(F.text == 'Назад↩️')
async def go_back(message: types.Message):
    logging.info(f"User {message.from_user.id} selected 'Назад'.")
    # Здесь возвращаем в предыдущее меню
    keyboard = answers_menu_kb()  # Убираем клавиатуру
    await message.answer('Повернення в головне меню', reply_markup=keyboard)
