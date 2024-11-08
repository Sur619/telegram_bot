import logging
from aiogram import types, Router, F
from keyboards.answers_menu import answers_menu_kb
from keyboards.testing import testing_menu_kb

menu_router = Router()


@menu_router.message(F.text == 'Тестування')
async def testing_cmd(message: types.Message):
    logging.info(f"User {message.from_user.id} selected 'Тестування'.")
    keyboard = testing_menu_kb()
    await message.answer("Виберіть тип тестування:", reply_markup=keyboard)


@menu_router.message(F.text == 'Пошук Відповідей')
async def answers_cmd(message: types.Message):
    logging.info(f"User {message.from_user.id} selected 'Пошук Відповідей'.")
    keyboard = answers_menu_kb()
    await message.answer('Оберіть опцію:', reply_markup=keyboard)
