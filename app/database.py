"""Підключення до бази даних та сесії SQLAlchemy."""

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.config import settings

engine = create_engine(settings.database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    """Базовий клас для всіх моделей."""


def get_db():
    """Видає сесію БД для одного запиту і гарантовано закриває її після."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
