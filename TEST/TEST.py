# from aiogram import Router, types, F
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
# from sqlalchemy import select, or_, func
# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy.orm import Session
#
# from database.models import GeneralTraining
# from keyboards.answers_menu import general_training_kb, answers_menu_kb
# import logging
#
# general_training_router = Router()
#
#
# # Handler for 'Загальнопрофільна підготовка' button
# @general_training_router.message(F.text == 'Загальнопрофільна підготовка')
# async def general_training(message: types.Message):
#     logging.info(f"User {message.from_user.id} selected 'Загальнопрофільна підготовка'.")
#     keyboard = general_training_kb()
#     await message.answer('Оберіть опцію:', reply_markup=keyboard)
#
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
#
#
# from sqlalchemy import func
#
#
# @general_training_router.message(F.text)
# async def search_questions(message: types.Message, session: AsyncSession):
#     query = message.text  # Оставляем оригинальный регистр, так как ilike сам по себе не чувствителен к регистру
#     logging.info(f"User {message.from_user.id} searching for '{query}'.")
#
#     stmt = select(GeneralTraining).where(
#         or_(
#             GeneralTraining.question.ilike(f"%{query}%"),
#             GeneralTraining.answer.ilike(f"%{query}%")
#         )
#     )
#     results = await session.execute(stmt)
#     questions = results.scalars().all()
#
#     if questions:
#         keyboard = InlineKeyboardMarkup(inline_keyboard=[])
#         for question in questions[:10]:
#             button_text = f"• {question.id}. {question.question[:30]}..."
#             keyboard.inline_keyboard.append(
#                 [InlineKeyboardButton(text=button_text, callback_data=f"show_{question.id}")])
#
#         await message.answer("Результаты поиска:", reply_markup=keyboard)
#     else:
#         await message.answer("Ничего не найдено.", reply_markup=types.ReplyKeyboardRemove())
#
#
# @general_training_router.callback_query(F.data.startswith("show_"))
# async def show_answer(callback_query: types.CallbackQuery, session: AsyncSession):
#     question_id = int(callback_query.data.split("_")[1])
#
#     result = await session.get(GeneralTraining, question_id)
#     if result:
#         await callback_query.message.answer(
#             f"• {result.question}\n\n{result.answer}"
#         )
#     else:
#         await callback_query.message.answer("Відповідь не знайдена.")
#
#     await callback_query.answer()
