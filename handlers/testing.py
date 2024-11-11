import logging

from aiogram import Router, F, types

from handlers.in_development import in_development
from keyboards import testing_menu_kb

testing_router = Router()


@testing_router.message(F.text == 'Тестування')
async def testing_cmd(message: types.Message):
    logging.info(f"User {message.from_user.id} selected 'Тестування'.")
    keyboard = testing_menu_kb()
    # await message.answer("Виберіть тип тестування:", reply_markup=keyboard)
    await in_development(message)
