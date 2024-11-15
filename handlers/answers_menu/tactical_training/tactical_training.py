from aiogram import Router, types, F
from sqlalchemy import select, or_
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import TacticalTraining
from handlers.serarch_in_db import search_in_database
from keyboards.answers_menu import tactical_training_kb
import logging

from keyboards.keyboard_for_search import create_keyboard

tactical_training_router = Router()


@tactical_training_router.message(F.text == 'Тактична підготовка')
async def tactical_training(message: types.Message):
    logging.info(f"User {message.from_user.id} selected 'Тактична підготовка'.")

    # Creating the tactical training keyboard
    keyboard = tactical_training_kb()
    await message.answer('Оберіть опцію:', reply_markup=keyboard)


@tactical_training_router.message(F.text == 'Назад◀️')
async def go_back(message: types.Message):
    from keyboards.answers_menu import answers_menu_kb
    keyboard = answers_menu_kb()
    logging.info(f"User {message.from_user.id} returned to the main menu.")
    await message.answer("Повернення в головне меню", reply_markup=keyboard)


@tactical_training_router.message(F.text)
async def search_questions(message: types.Message, session: AsyncSession):
    query = message.text
    exclude_keywords = ["Загальнопрофільна підготовка", "Назад◀️", "Тактична підготовка",
                        "Функціональна підготовка", "Вогнева підготовка", "Додаткові заняття"]

    results = await search_in_database(
        session=session,
        model=TacticalTraining,
        query=query,
        exclude_keywords=exclude_keywords
    )

    if results is None:
        logging.info(f"User {message.from_user.id} selected a command, skipping search: '{query}'.")
        return

    if results:
        keyboard = await create_keyboard(results)
        await message.answer("Результаты поиска:", reply_markup=keyboard)
    else:
        await message.answer("Ничего не найдено.", reply_markup=types.ReplyKeyboardRemove())


@tactical_training_router.callback_query(F.data.startswith("show_"))
async def show_answer(callback_query: types.CallbackQuery, session: AsyncSession):
    try:
        question_id = int(callback_query.data.split("_")[1])  # Безопасный парсинг ID вопроса
    except (IndexError, ValueError):
        await callback_query.message.answer("Некорректный запрос.")
        await callback_query.answer()
        return

    result = await session.get(TacticalTraining, question_id)
    if result:
        await callback_query.message.answer(
            f"• {result.question}\n\n{result.answer}"
        )
    else:
        await callback_query.message.answer("Відповідь не знайдена.")

    await callback_query.answer()
