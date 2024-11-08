import os
import logging
from aiogram import types, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import FSInputFile
from bot_instance import bot
from keyboards.main_menu import main_menu_kb

logging.basicConfig(level=logging.INFO)

start_router = Router()


@start_router.message(CommandStart())
@start_router.message(Command('menu'))
async def start_cmd(message: types.Message):
    video_path = 'D:/Python/Django/Projects/Telegram_bot/content/video.mp4'
    logging.info(f"User {message.from_user.id} started the bot with /start or /menu.")

    try:
        if os.path.exists(video_path):
            video = FSInputFile(video_path, filename='video.mp4')
            await bot.send_video(chat_id=message.chat.id, video=video)
    except Exception as e:
        logging.error(f"Error sending video: {e}")

    await message.answer(
        f"{message.from_user.first_name}, вітаємо!\n"
        "Перед початком роботи з ботом ознайомтесь з розділом \"Правила користування\"."
    )
    keyboard = main_menu_kb()
    await message.answer("Оберіть опцію:", reply_markup=keyboard)
