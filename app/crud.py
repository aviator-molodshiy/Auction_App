"""Функції роботи з базою даних. Вони нічого не знають про HTTP."""

from sqlalchemy import select
from sqlalchemy.orm import Session

from app import models


def list_containers(db: Session, skip: int, limit: int) -> list[models.Container]:
    query = select(models.Container).order_by(models.Container.id).offset(skip).limit(limit)
    return list(db.scalars(query).all())


def get_container_by_name(db: Session, name: str) -> models.Container | None:
    return db.scalar(select(models.Container).where(models.Container.name == name))


def create_container(db: Session, name: str) -> models.Container:
    container = models.Container(name=name)
    db.add(container)
    db.commit()
    db.refresh(container)
    return container


def delete_container(db: Session, container: models.Container) -> None:
    db.delete(container)
    db.commit()


def create_item(db: Session, container: models.Container, name: str, price: float) -> models.Item:
    item = models.Item(name=name, price=price, container_id=container.id)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def list_items(db: Session, skip: int, limit: int) -> list[models.Item]:
    query = select(models.Item).order_by(models.Item.id).offset(skip).limit(limit)
    return list(db.scalars(query).all())


def get_item(db: Session, item_id: int) -> models.Item | None:
    return db.get(models.Item, item_id)


def update_item(
    db: Session, item: models.Item, name: str | None, price: float | None
) -> models.Item:
    """Змінює лише ті поля, які передали (не None)."""
    if name is not None:
        item.name = name
    if price is not None:
        item.price = price
    db.commit()
    db.refresh(item)
    return item


def delete_item(db: Session, item: models.Item) -> None:
    db.delete(item)
    db.commit()
