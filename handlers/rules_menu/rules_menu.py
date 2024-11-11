import logging

from aiogram import Router, F, types

from handlers.in_development import in_development
from keyboards.rules_menu import rules_menu_kb

rules_menu_router = Router()


@rules_menu_router.message(F.text == 'Правила користування')
async def answers_cmd(message: types.Message):
    logging.info(f"User {message.from_user.id} selected 'Правила користування'.")
    keyboard = rules_menu_kb()
    await message.answer(
        f"🔶Основні правила бота\n"
        "Звертаємо увагу, що бот створений виключно з метою підвищення рівня знань.\n"
        "Пошук правильних відповідей створено з метою аналізу допущених помилок.\n"
        "Користування ботом та пошук відповідей під час проходження тестування суворо заборонено!\n\n"
        "🔶Інформація про захист особистих даних та гарантії покупця\n"
        "Бот не використовує, не оброблює та не зберігає жодну інформацію персональних даних користувача! \n"
        "Усі реквізити карт оброблюються тільки платіжною системою «Fondy» та вашим банком. \n"
        "Усі дані покупця, які передаються через мережу - надійно захищені та шифруються. \n"
        "Після оплати - ви автоматично отримаєте увесь пакет послуг, а також отримаєте відповідне повідомлення про те, що вам були надані VIP-послуги.\n\n"
        "🔶Якщо у вас виникли питання щодо підписки та оплати - зверніться за допомогою, натиснувши кнопку \n"
        "\"Повідомити про помилку🖍\" нижче, або напишіть нам у відділ підтримки на пошту questions.nputest@gmail.com",
        reply_markup=keyboard
    )


@rules_menu_router.message(F.text == 'Найчастіші запитання❓')
async def answers_cmd(message: types.Message):
    logging.info(f"User {message.from_user.id} selected 'Найчастіші запитання❓'.")
    keyboard = rules_menu_kb()
    await in_development(message)


@rules_menu_router.message(F.text == 'Повідомити про помилку🖍')
async def answers_cmd(message: types.Message):
    logging.info(f"User {message.from_user.id} selected 'Повідомити про помилку🖍'.")
    keyboard = rules_menu_kb()
    await in_development(message)
