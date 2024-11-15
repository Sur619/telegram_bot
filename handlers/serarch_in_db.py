from sqlalchemy import select, or_
from sqlalchemy.ext.asyncio import AsyncSession

async def search_in_table(
        session: AsyncSession,
        model,  # SQLAlchemy модель таблицы
        query: str  # Текст для поиска
):
    stmt = select(model).where(
        or_(
            model.question.ilike(f"%{query}%"),  # Поиск по полю 'question'
            model.answer.ilike(f"%{query}%")  # Поиск по полю 'answer'
        )
    )
    results = await session.execute(stmt)
    return results.scalars().all()
