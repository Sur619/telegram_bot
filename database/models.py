from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


# Определяем базовый класс для моделей
class Base(DeclarativeBase):
    pass


# Модель GeneralTraining
class GeneralTraining(Base):
    __tablename__ = 'general_training'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)  # auto-increment is implicit
    question: Mapped[str] = mapped_column(Text)
    answer: Mapped[str] = mapped_column(Text)
    variables: Mapped[str] = mapped_column(Text, nullable=True)


class TacticalTraining(Base):
    __tablename__ = 'tactical_training'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)  # auto-increment is implicit
    question: Mapped[str] = mapped_column(Text)
    answer: Mapped[str] = mapped_column(Text)
    variables: Mapped[str] = mapped_column(Text, nullable=True)


class FunctionalTraining(Base):
    __tablename__ = 'functional_training'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)  # auto-increment is implicit
    question: Mapped[str] = mapped_column(Text)
    answer: Mapped[str] = mapped_column(Text)
    variables: Mapped[str] = mapped_column(Text, nullable=True)


class AdditionalQuestion(Base):
    __tablename__ = 'additional_question'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)  # auto-increment is implicit
    question: Mapped[str] = mapped_column(Text)
    answer: Mapped[str] = mapped_column(Text)
    variables: Mapped[str] = mapped_column(Text, nullable=True)
