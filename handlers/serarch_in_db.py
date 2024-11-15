from sqlalchemy import select, or_
from sqlalchemy.ext.asyncio import AsyncSession

async def search_in_database(
    session: AsyncSession,
    model,  # SQLAlchemy модель таблицы
    query: str,  # Запрос для поиска
    exclude_keywords: list[str]  # Список исключаемых текстов
):
    """
    Выполняет поиск в базе данных для указанной модели.

    :param session: Сессия SQLAlchemy
    :param model: Модель SQLAlchemy, в которой выполняется поиск
    :param query: Текст поиска
    :param exclude_keywords: Список ключевых слов, которые не должны обрабатываться
    :return: Список результатов поиска
    """
    if query in exclude_keywords:
        return None  # Пропустить команды или исключенные тексты

    stmt = select(model).where(
        or_(
            model.question.ilike(f"%{query}%"),
            model.answer.ilike(f"%{query}%")
        )
    )
    results = await session.execute(stmt)
    return results.scalars().all()
