import logging
from aiogram import types, Router
from aiogram.filters import Command

from handlers.in_development import in_development

info_router = Router()


@info_router.message(Command('about'))
async def about_cmd(message: types.Message):
    logging.info(f"User {message.from_user.id} requested 'about' info.")
    # await message.answer("its about us")
    await in_development(message)


@info_router.message(Command('payment'))
async def payment_cmd(message: types.Message):
    logging.info(f"User {message.from_user.id} requested 'payment' info.")
    # await message.answer("its about payment")
    await in_development(message)
