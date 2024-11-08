import logging
from aiogram import types, Router, F
from keyboards.answers_menu import answers_menu_kb

menu_router = Router()


@menu_router.message(F.text == 'Пошук Відповідей')
async def answers_cmd(message: types.Message):
    logging.info(f"User {message.from_user.id} selected 'Пошук Відповідей'.")
    keyboard = answers_menu_kb()
    await message.answer('Оберіть опцію:', reply_markup=keyboard)


@menu_router.message(F.text == 'Термін дії моєї підписки')
async def answers_cmd(message: types.Message):
    logging.info(f"User {message.from_user.id} selected 'Термін дії моєї підписки'.")
    keyboard = answers_menu_kb()
    await message.answer('Оберіть опцію:', reply_markup=keyboard)


@menu_router.message(F.text == 'Придбати VIP доступ')
async def answers_cmd(message: types.Message):
    logging.info(f"User {message.from_user.id} selected 'Придбати VIP доступ'.")
    keyboard = answers_menu_kb()
    await message.answer('Оберіть опцію:', reply_markup=keyboard)


@menu_router.message(F.text == 'Правила користування')
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