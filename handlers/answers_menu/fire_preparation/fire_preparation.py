# from aiogram import Router, types, F
#
# from handlers.in_development import in_development
# from keyboards.answers_menu import answers_menu_kb
# import logging
# from aiogram.types import CallbackQuery
#
# fire_preparation_router = Router()
#
#
# # Handler for 'Загальнопрофільна підготовка' button
# @fire_preparation_router.message(F.text == 'Вогнева підготовка')
# async def fire_preparation(message: types.Message):
#     logging.info(f"User {message.from_user.id} selected 'Вогнева підготовка'.")
#     keyboard = answers_menu_kb()
#     await in_development(message, keyboard=keyboard)
