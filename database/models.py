from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class GeneralTraining(Base):
    __tablename__ = 'general_training'
    id = Mapped[int] = mapped_column(primary_key=True, auto_increment=True)
    question = Mapped[str] = mapped_column(Text)
    answer = Mapped[str] = mapped_column(Text)
    variables = Mapped[str] = mapped_column(Text)
