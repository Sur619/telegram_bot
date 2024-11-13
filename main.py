import asyncio
import logging
from aiogram import Dispatcher, types
from bot_instance import bot  # Импорт бота из отдельного файла
from common.bot_cmd_list import private  # Импорт списка команд
from database.engine import create_db, drop_db, session_maker
from handlers import start, menu, info, answers_menu, rules_menu
from handlers.answers_menu import general_training
from middlewares.db import DataBaseSession

# Конфигурируем логирование
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Перечень разрешенных обновлений
# ALLOWED_UPDATES = ['message', 'edited_message', 'callback_query']

# Инициализация диспетчера и добавление роутера
dp = Dispatcher()
# Подключение всех маршрутов из отдельных модулей
dp.include_routers(start.start_router, menu.menu_router, answers_menu.general_training_router, info.info_router,
                   rules_menu.rules_menu_router, answers_menu.fire_preparation_router,
                   answers_menu.functional_training_router,
                   answers_menu.tactical_training_router, answers_menu.additional_question_router)


async def on_startup(bot):
    run_param = False
    if run_param:
        await drop_db()

    await create_db()


async def on_shutdown(bot):
    print('Shutting down...')


async def main() -> None:
    try:
        dp.startup.register(on_startup)
        dp.shutdown.register(on_shutdown)
        dp.update.middleware(DataBaseSession(session_pool=session_maker))
        # Удаляем вебхук и настраиваем команды
        await bot.delete_webhook(drop_pending_updates=True)
        await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())

        # Запускаем поллинг
        logger.info("Starting bot polling...")
        await dp.start_polling(bot)#allowed_updates=ALLOWED_UPDATES


    except Exception as e:
        logger.error(f"Error occurred: {e}")

    finally:
        # Закрываем соединение с ботом при завершении работы
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
