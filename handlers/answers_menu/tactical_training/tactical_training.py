from aiogram import Router, types, F
from sqlalchemy import select, or_
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import TacticalTraining
from keyboards.answers_menu import tactical_training_kb
import logging

from keyboards.keyboard_for_search import create_keyboard

tactical_training_router = Router()


@tactical_training_router.message(F.text == 'Тактична підготовка')
async def tactical_training(message: types.Message):
    logging.info(f"User {message.from_user.id} selected 'Тактична підготовка'.")
    keyboard = tactical_training_kb()
    await message.answer('Оберіть опцію:', reply_markup=keyboard)


@tactical_training_router.message(F.text)
async def search_questions(message: types.Message, session: AsyncSession):
    query = message.text
    logging.info(f"User {message.from_user.id} searching for '{query}'.")

    stmt = select(TacticalTraining).where(
        or_(
            TacticalTraining.question.ilike(f"%{query}%"),
            TacticalTraining.answer.ilike(f"%{query}%")
        )
    )
    results = await session.execute(stmt)
    questions = results.scalars().all()

    if questions:
        keyboard = await create_keyboard(questions)
        await message.answer("Результаты поиска:", reply_markup=keyboard)
    else:
        await message.answer("Ничего не найдено.", reply_markup=types.ReplyKeyboardRemove())


# Callback handler to show the answer for a selected question
@tactical_training_router.callback_query(F.data.startswith("show_"))
async def show_answer(callback_query: types.CallbackQuery, session: AsyncSession):
    try:
        question_id = int(callback_query.data.split("_")[1])  # Parse the question ID safely
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
