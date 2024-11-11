import logging
from aiogram import types, Router, F

from handlers.in_development import in_development
from keyboards.answers_menu import answers_menu_kb
from keyboards.rules_menu import rules_menu_kb

menu_router = Router()


@menu_router.message(F.text == 'Пошук Відповідей')
async def answers_cmd(message: types.Message):
    logging.info(f"User {message.from_user.id} selected 'Пошук Відповідей'.")
    keyboard = answers_menu_kb()
    await message.answer('Оберіть опцію:', reply_markup=keyboard)


@menu_router.message(F.text == 'Термін дії моєї підписки')
async def answers_cmd(message: types.Message):
    logging.info(f"User {message.from_user.id} selected 'Термін дії моєї підписки'.")
    keyboard = answers_menu_kb()
    # await message.answer('Оберіть опцію:', reply_markup=keyboard)
    await in_development(message)


@menu_router.message(F.text == 'Придбати VIP доступ')
async def answers_cmd(message: types.Message):
    logging.info(f"User {message.from_user.id} selected 'Придбати VIP доступ'.")
    keyboard = answers_menu_kb()
    # await message.answer('Оберіть опцію:', reply_markup=keyboard)
    await in_development(message)


