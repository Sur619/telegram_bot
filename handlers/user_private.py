import os
from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import FSInputFile
from bot_instance import bot

user_private_router = Router()


# Головне меню
async def main_menu(message: types.Message):
    # Створення клавіатури
    kb = [
        [
            types.KeyboardButton(text="Тестування"),
            types.KeyboardButton(text="Пошук Відповідей"),
        ],
        [
            types.KeyboardButton(text="Термін дії моєї підписки"),
            types.KeyboardButton(text="Придбати VIP доступ"),
        ],
        [types.KeyboardButton(text="Правила користування")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Оберіть опцію:", reply_markup=keyboard)


# Команда /start
@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    video_path = 'D:/Python/Django/Projects/Telegram_bot/content/video.mp4'

    # Відправлення відео, якщо файл існує
    if os.path.exists(video_path):
        video = FSInputFile(video_path, filename='video.mp4')
        await bot.send_video(chat_id=message.chat.id, video=video)

    # Привітальне повідомлення
    await message.answer(
        f"{message.from_user.first_name}, вітаємо!\n"
        "Перед початком роботи з ботом ознайомтесь з розділом \"Правила користування\".\n"
        "Безкоштовний доступ надає вам пошук у темі \"Безпека життєдіяльності\".\n"
        "Ви також можете запросити до нашого боту друзів за допомогою свого індивідуального посилання!"
    )

    # Переходимо до головного меню
    await main_menu(message)


@user_private_router.message(F.text == 'Тестування')
async def test_cmd(message: types.Message):
    kb = [
        [types.KeyboardButton(text='Види тестування')],
        [types.KeyboardButton(text='У головне меню')]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Виберіть тип тестування:", reply_markup=keyboard)


@user_private_router.message(F.text.in_(['У головне меню', 'Меню']))
async def back_to_main_menu(message: types.Message):
    # Повернення до головного меню
    await main_menu(message)


@user_private_router.message(CommandStart())
@user_private_router.message(Command('menu'))
async def menu_cmd(message: types.Message):
    await message.answer("its menu")


@user_private_router.message(Command('about'))
async def about_cmd(message: types.Message):
    await message.answer("its about us")


@user_private_router.message(Command('payment'))
async def payment_cmd(message: types.Message):
    await message.answer("its about payment")
