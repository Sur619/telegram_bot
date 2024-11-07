# D:\Python\Django\Projects\Telegram_bot\app.py
import asyncio
from aiogram import Dispatcher, types
from aiogram.types import InputFile
from bot_instance import bot
from common.bot_cmd_list import private
from handlers.user_private import user_private_router

ALLOWED_UPDATES = ['message', 'edited_message', 'types.Update', 'types.CallbackQuery']

dp = Dispatcher()
dp.include_router(user_private_router)


async def main() -> None:
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


asyncio.run(main())
