"""Точка входу: створює застосунок FastAPI і підключає роутери."""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from app import models  # noqa: F401  (імпорт потрібен, щоб SQLAlchemy знала про таблиці)
from app.database import Base, engine
from app.routers import containers, items


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Створюємо таблиці при старті. Пізніше це замінять міграції Alembic.
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title="Auction Manager API", version="2.0.0", lifespan=lifespan)


@app.get("/", tags=["service"])
def hello():
    return {"message": "Auction Manager API працює"}


@app.get("/health", tags=["service"])
def health():
    return {"status": "ok"}


app.include_router(containers.router)
app.include_router(items.router)
