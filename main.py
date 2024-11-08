import asyncio
import logging
from aiogram import Dispatcher, types
from bot_instance import bot  # Импорт бота из отдельного файла
from common.bot_cmd_list import private  # Импорт списка команд
from handlers import start, menu, answers, info

# Конфигурируем логирование
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Перечень разрешенных обновлений
ALLOWED_UPDATES = ['message', 'edited_message', 'callback_query']

# Инициализация диспетчера и добавление роутера
dp = Dispatcher()
# Подключение всех маршрутов из отдельных модулей
dp.include_router(start.start_router)  # Обработчики команды /start и меню
dp.include_router(menu.menu_router)  # Обработчики кнопок главного меню
dp.include_router(answers.answers_router)  # Обработчики меню 'Пошук Відповідей'
dp.include_router(info.info_router)  # Обработчики команд /about и /payment


async def main() -> None:
    try:
        # Удаляем вебхук и настраиваем команды
        await bot.delete_webhook(drop_pending_updates=True)
        await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())

        # Запускаем поллинг
        logger.info("Starting bot polling...")
        await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)

    except Exception as e:
        logger.error(f"Error occurred: {e}")

    finally:
        # Закрываем соединение с ботом при завершении работы
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
