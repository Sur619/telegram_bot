# D:\Python\Django\Projects\Telegram_bot\bot_instance.py
import os
from aiogram import Bot
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

bot = Bot(token=os.getenv("BOT_TOKEN"))
