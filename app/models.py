"""Моделі таблиць: контейнери та речі в них."""

from sqlalchemy import Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Container(Base):
    __tablename__ = "containers"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, unique=True)

    # При видаленні контейнера його речі видаляються разом з ним
    items: Mapped[list["Item"]] = relationship(
        back_populates="container", cascade="all, delete-orphan"
    )


class Item(Base):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String)
    price: Mapped[float] = mapped_column(Float)
    container_id: Mapped[int] = mapped_column(ForeignKey("containers.id"))

    container: Mapped["Container"] = relationship(back_populates="items")
