from aiogram import Router, types, F
from sqlalchemy.ext.asyncio import AsyncSession
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from database.models import GeneralTraining, TacticalTraining
from handlers.serarch_in_db import search_in_table
from keyboards.answers_menu import general_training_kb, tactical_training_kb, answers_menu_kb
from keyboards.keyboard_for_search import create_keyboard
import logging

router = Router()

# Карта моделей базы данных для каждой кнопки
MODEL_MAP = {
    "Загальнопрофільна підготовка": (GeneralTraining, general_training_kb),
    "Тактична підготовка": (TacticalTraining, tactical_training_kb),
}


# Состояние для активной модели
class SearchState(StatesGroup):
    active_model = State()
    selected_option = State()  # Для выделения выбранной опции


# Обработчик для выбора раздела
@router.message(F.text.in_(MODEL_MAP.keys()))
async def select_section(message: types.Message, state: FSMContext):
    # Извлекаем модель и функцию клавиатуры
    model, kb_func = MODEL_MAP[message.text]
    await state.update_data(active_model=model, selected_option=None)

    # Логируем выбор пользователя
    logging.info(f"User {message.from_user.id} selected section: {message.text}")

    # Генерируем и отправляем клавиатуру
    keyboard = kb_func()
    await message.answer(f"Ви обрали розділ '{message.text}'. Введіть текст для пошуку:", reply_markup=keyboard)


# Обработчик для кнопок выбора внутри раздела
@router.message(
    F.text.in_(["Безпека життєдіяльності", "Домедична підготовка", "Психологічна підготовка", "Тактика дій"])
)
async def process_selected_option(message: types.Message, state: FSMContext):
    selected_option = message.text
    await state.update_data(selected_option=selected_option)

    # Логируем выбор
    logging.info(f"User {message.from_user.id} selected option: {selected_option}")

    # Обновляем клавиатуру с выделенной кнопкой
    data = await state.get_data()
    active_model = data.get("active_model")
    if not active_model:
        await message.answer("Будь ласка, оберіть розділ перед пошуком.", reply_markup=types.ReplyKeyboardRemove())
        return

    keyboard = general_training_kb(selected_option) if active_model == GeneralTraining else tactical_training_kb(
        selected_option)
    await message.answer(
        "Введіть запитання або ключові слова🔎\n"
        "Увага! Для швидкого і коректного пошуку введіть запитання повністю.",
        reply_markup=keyboard
    )


# Обработчик для кнопки "Назад◀️"
@router.message(F.text == 'Назад◀️')
async def go_back(message: types.Message):
    keyboard = answers_menu_kb()  # Возвращаем главное меню
    logging.info(f"User {message.from_user.id} returned to the main menu.")
    await message.answer('Повернення в головне меню', reply_markup=keyboard)


# Обработчик для поиска текста
@router.message(F.text)
async def search_questions(message: types.Message, state: FSMContext, session: AsyncSession):
    # Получаем текущую модель из состояния
    data = await state.get_data()
    active_model = data.get("active_model")
    if not active_model:
        await message.answer("Будь ласка, оберіть розділ перед пошуком.", reply_markup=types.ReplyKeyboardRemove())
        return

    query = message.text
    logging.info(f"User {message.from_user.id} searching for '{query}' in {active_model.__name__}.")
    results = await search_in_table(session, active_model, query)

    if results:
        keyboard = await create_keyboard(results)
        await message.answer("Результаты пошуку:", reply_markup=keyboard)
    else:
        await message.answer("Нічого не знайдено.", reply_markup=types.ReplyKeyboardRemove())
