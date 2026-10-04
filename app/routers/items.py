"""Ендпоінти для речей."""

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db
from app.validation import clean_name

router = APIRouter(prefix="/items", tags=["items"])


def get_item_or_404(item_id: int, db: Session = Depends(get_db)):
    item = crud.get_item(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Річ не знайдено")
    return item


@router.get("", response_model=list[schemas.ItemRead])
def list_items(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=100),
    db: Session = Depends(get_db),
):
    return crud.list_items(db, skip, limit)


@router.get("/{item_id}", response_model=schemas.ItemRead)
def get_item(item=Depends(get_item_or_404)):
    return item


@router.patch("/{item_id}", response_model=schemas.ItemRead)
def update_item(
    item_name: str | None = Query(None, max_length=100, description="Нова назва (необов'язково)"),
    item_price: float | None = Query(None, gt=0, description="Нова ціна (необов'язково)"),
    item=Depends(get_item_or_404),
    db: Session = Depends(get_db),
):
    name = clean_name(item_name) if item_name is not None else None
    return crud.update_item(db, item, name, item_price)


@router.delete("/{item_id}", status_code=204)
def delete_item(item=Depends(get_item_or_404), db: Session = Depends(get_db)):
    crud.delete_item(db, item)
