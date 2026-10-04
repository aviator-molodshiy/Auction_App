"""Ендпоінти для контейнерів."""

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db
from app.validation import clean_name

router = APIRouter(prefix="/containers", tags=["containers"])


@router.get("", response_model=list[schemas.ContainerRead])
def list_containers(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=100),
    db: Session = Depends(get_db),
):
    return crud.list_containers(db, skip, limit)


@router.post("", response_model=schemas.ContainerRead, status_code=201)
def create_container(
    name: str = Query(..., max_length=100, description="Назва контейнера"),
    db: Session = Depends(get_db),
):
    name = clean_name(name)
    if crud.get_container_by_name(db, name):
        raise HTTPException(status_code=409, detail="Контейнер з такою назвою вже існує")
    return crud.create_container(db, name)


@router.get("/{container_name}", response_model=schemas.ContainerRead)
def get_container(container_name: str, db: Session = Depends(get_db)):
    container = crud.get_container_by_name(db, container_name)
    if container is None:
        raise HTTPException(status_code=404, detail="Контейнер не знайдено")
    return container


@router.delete("/{container_name}", status_code=204)
def delete_container(container_name: str, db: Session = Depends(get_db)):
    container = crud.get_container_by_name(db, container_name)
    if container is None:
        raise HTTPException(status_code=404, detail="Контейнер не знайдено")
    crud.delete_container(db, container)


@router.post("/{container_name}/items", response_model=schemas.ItemRead, status_code=201)
def add_item(
    container_name: str,
    item_name: str = Query(..., max_length=100, description="Назва речі"),
    item_price: float = Query(..., gt=0, description="Ціна, більша за нуль"),
    db: Session = Depends(get_db),
):
    """Додає річ у контейнер. Якщо контейнера ще немає, він створюється автоматично."""
    container_name = clean_name(container_name)
    item_name = clean_name(item_name)

    container = crud.get_container_by_name(db, container_name)
    if container is None:
        container = crud.create_container(db, container_name)
    return crud.create_item(db, container, item_name, item_price)
