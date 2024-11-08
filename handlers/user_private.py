# import os
# from aiogram import types, Router, F
# from aiogram.filters import CommandStart, Command
# from aiogram.types import FSInputFile
# from bot_instance import bot
# import logging
#
# # Setting up logging
# logging.basicConfig(level=logging.INFO)
#
# user_private_router = Router()
#
#
# # Function to create the main menu keyboard
# def create_main_menu_keyboard():
#     kb = [
#         [
#             types.KeyboardButton(text="Тестування"),
#             types.KeyboardButton(text="Пошук Відповідей"),
#         ],
#         [
#             types.KeyboardButton(text="Термін дії моєї підписки"),
#             types.KeyboardButton(text="Придбати VIP доступ"),
#         ],
#         [types.KeyboardButton(text="Правила користування")]
#     ]
#     return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
#
#
# # Main menu function
# async def main_menu(message: types.Message):
#     keyboard = create_main_menu_keyboard()
#     await message.answer("Оберіть опцію:", reply_markup=keyboard)
#
#
# # Combined handler for /start and /menu commands
# @user_private_router.message(CommandStart())
# @user_private_router.message(Command('menu'))
# async def start_cmd(message: types.Message):
#     video_path = 'D:/Python/Django/Projects/Telegram_bot/content/video.mp4'
#     logging.info(f"User {message.from_user.id} started the bot with /start or /menu.")
#
#     # Send video if the file exists
#     try:
#         if os.path.exists(video_path):
#             video = FSInputFile(video_path, filename='video.mp4')
#             await bot.send_video(chat_id=message.chat.id, video=video)
#     except Exception as e:
#         logging.error(f"Error sending video: {e}")
#
#     # Welcome message
#     await message.answer(
#         f"{message.from_user.first_name}, вітаємо!\n"
#         "Перед початком роботи з ботом ознайомтесь з розділом \"Правила користування\".\n"
#         "Безкоштовний доступ надає вам пошук у темі \"Безпека життєдіяльності\".\n"
#         "Ви також можете запросити до нашого боту друзів за допомогою свого індивідуального посилання!"
#     )
#
#     # Go to main menu
#     await main_menu(message)
#
#
# # Handler for 'Тестування' button
# @user_private_router.message(F.text == 'Тестування')
# async def testing_cmd(message: types.Message):
#     logging.info(f"User {message.from_user.id} selected 'Тестування'.")
#     kb = [
#         [types.KeyboardButton(text='Види тестування')],
#         [types.KeyboardButton(text='У головне меню')]
#     ]
#     keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
#     await message.answer("Виберіть тип тестування:", reply_markup=keyboard)
#
#
# # Handler for 'Пошук Відповідей' button
# @user_private_router.message(F.text == 'Пошук Відповідей')
# async def answers_cmd(message: types.Message):
#     logging.info(f"User {message.from_user.id} selected 'Пошук Відповідей'.")
#     kb = [
#         [
#             types.KeyboardButton(text='Загальнопрофільна підготовка'),
#             types.KeyboardButton(text='Вогнева підготовка')
#         ],
#         [
#             types.KeyboardButton(text='Тактична підготовка'),
#             types.KeyboardButton(text='Функціональна підготовка')
#         ],
#         [
#             types.KeyboardButton(text='У головне меню')
#         ]
#     ]
#     keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
#     await message.answer('Оберіть опцію:', reply_markup=keyboard)
#
#
# # Handler for 'Загальнопрофільна підготовка' button
# @user_private_router.message(F.text == 'Загальнопрофільна підготовка')
# async def answers1_cmd(message: types.Message):
#     logging.info(f"User {message.from_user.id} selected 'Загальнопрофільна підготовка'.")
#     kb = [
#         [types.KeyboardButton(text='Безпека життєдіяльності')],
#         [types.KeyboardButton(text='Домедична підготовка')],
#         [types.KeyboardButton(text='Психологічна підготовка')],
#         [types.KeyboardButton(text='Назад')]  # Back button to go to 'Пошук Відповідей'
#     ]
#     keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
#     await message.answer('Оберіть опцію:', reply_markup=keyboard)
#
#
# # Handler for 'Безпека життєдіяльності' button
# @user_private_router.message(F.text == 'Безпека життєдіяльності')
# async def safety_cmd(message: types.Message):
#     logging.info(f"User {message.from_user.id} selected 'Безпека життєдіяльності'.")
#     await message.answer(
#         "Введіть запитання або ключові слова🔎\nУвага! Для швидкого і коректного пошуку введіть запитання повністю")
#
#
# # Handler for 'Домедична підготовка' button
# @user_private_router.message(F.text == 'Домедична підготовка')
# async def medical_cmd(message: types.Message):
#     logging.info(f"User {message.from_user.id} selected 'Домедична підготовка'.")
#     await message.answer(
#         "Введіть запитання або ключові слова🔎\nУвага! Для швидкого і коректного пошуку введіть запитання повністю")
#
#
# # Handler for 'Психологічна підготовка' button
# @user_private_router.message(F.text == 'Психологічна підготовка')
# async def psychology_cmd(message: types.Message):
#     logging.info(f"User {message.from_user.id} selected 'Психологічна підготовка'.")
#     await message.answer(
#         "Введіть запитання або ключові слова🔎\nУвага! Для швидкого і коректного пошуку введіть запитання повністю")
#
#
# # Handler for 'Назад' button in 'Загальнопрофільна підготовка' submenu
# @user_private_router.message(F.text == 'Назад')
# async def back_to_answers_cmd(message: types.Message):
#     logging.info(f"User {message.from_user.id} selected 'Назад' in 'Загальнопрофільна підготовка'.")
#     await answers_cmd(message)  # Calls the 'answers_cmd' function to return to the previous menu
#
#
# # Handler to go back to the main menu
# @user_private_router.message(F.text.in_(['У головне меню', 'Меню']))
# async def back_to_main_menu(message: types.Message):
#     logging.info(f"User {message.from_user.id} returned to the main menu.")
#     await main_menu(message)
#
#
# # About command
# @user_private_router.message(Command('about'))
# async def about_cmd(message: types.Message):
#     logging.info(f"User {message.from_user.id} requested 'about' info.")
#     await message.answer("its about us")
#
#
# # Payment command
# @user_private_router.message(Command('payment'))
# async def payment_cmd(message: types.Message):
#     logging.info(f"User {message.from_user.id} requested 'payment' info.")
#     await message.answer("its about payment")
