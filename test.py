import os

from aiogram.types import message

video_path = 'D:/Python/Django/Projects/Telegram_bot/content/video.mp4'

if os.path.exists(video_path):
    with open(video_path, 'rb') as video_file:
        await message.answer_video(video_file, caption="Ось ваше відео!")
else:
    await message.answer("Вибачте, відео не знайдено.")
