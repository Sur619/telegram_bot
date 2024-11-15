# from aiogram import Router, types, F
#
# from handlers.in_development import in_development
# from keyboards.answers_menu import answers_menu_kb
# import logging
# from aiogram.types import CallbackQuery
#
# functional_training_router = Router()
#
#
# # Handler for 'Загальнопрофільна підготовка' button
# @functional_training_router.message(F.text == 'Функціональна підготовка')
# async def functional_training(message: types.Message):
#     logging.info(f"User {message.from_user.id} selected 'Функціональна підготовка'.")
#     keyboard = answers_menu_kb()
#     await in_development(message, keyboard=keyboard)
