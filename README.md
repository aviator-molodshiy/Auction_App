# Auction Manager API

Backend-сервер для керування аукціонними контейнерами та речами в них.

## Стек технологій

- Python 3.12+
- FastAPI: веб-фреймворк
- PostgreSQL: база даних
- SQLAlchemy 2.0: ORM
- Pydantic: валідація даних
- Docker Compose: запуск одною командою
- pytest: автотести

## Можливості

- Повний CRUD для контейнерів і речей
- Автоматичне створення контейнера, якщо його ще не існує
- Проста робота через `/docs`: усі дані вводяться окремими полями, без JSON
- Валідація вхідних даних (непорожня назва, ціна більша за нуль)
- Пагінація списків (`skip`, `limit`)
- Правильні HTTP-статуси: 201, 204, 404, 409, 422
- Налаштування через змінні середовища, без паролів у коді
- Автотести на окремій базі в пам'яті, справжню базу вони не чіпають

## Структура проєкту

```
app/
  main.py          # створення застосунку та підключення роутерів
  config.py        # налаштування зі змінних середовища (.env)
  database.py      # підключення до БД і сесії
  models.py        # таблиці SQLAlchemy
  schemas.py       # схеми відповідей (Pydantic)
  validation.py    # спільні перевірки введених даних
  crud.py          # робота з базою даних
  routers/
    containers.py  # ендпоінти контейнерів
    items.py       # ендпоінти речей
tests/             # автотести
Dockerfile
docker-compose.yml
```

## Швидкий запуск через Docker

1. Скопіюй `.env.example` у `.env` і вкажи свій пароль до бази.
2. Запусти: `docker compose up --build`
3. Відкрий документацію API: http://127.0.0.1:8000/docs

## Запуск без Docker

1. Створи базу `auction_db` у своєму PostgreSQL.
2. Скопіюй `.env.example` у `.env` і вкажи в `DATABASE_URL` свої дані.
3. Встанови залежності: `pip install -r requirements.txt`
4. Запусти сервер: `uvicorn app.main:app --reload`
5. Відкрий http://127.0.0.1:8000/docs

## Тести

```
pip install -r requirements-dev.txt
pytest
```

## API

| Метод | Адреса | Що робить |
|-------|--------|-----------|
| GET | `/` | Перевірка, що сервер працює |
| GET | `/health` | Стан сервісу |
| GET | `/containers` | Список контейнерів (`skip`, `limit`) |
| POST | `/containers?name=...` | Створити порожній контейнер |
| GET | `/containers/{name}` | Один контейнер з його речами |
| DELETE | `/containers/{name}` | Видалити контейнер разом з речами |
| POST | `/containers/{name}/items?item_name=...&item_price=...` | Додати річ (контейнер створиться сам) |
| GET | `/items` | Список речей (`skip`, `limit`) |
| GET | `/items/{id}` | Одна річ |
| PATCH | `/items/{id}?item_name=...&item_price=...` | Змінити назву та/або ціну |
| DELETE | `/items/{id}` | Видалити річ |

Приклад додавання речі:

```
POST /containers/Box-1/items?item_name=Годинник&item_price=150.5
```

У `/docs` достатньо вписати назву контейнера, назву речі та ціну в окремі поля.

## Плани

- Користувачі та JWT-авторизація
- Ставки на лоти
- Міграції бази даних через Alembic

## Автор

Орест: https://github.com/aviator-molodshiy
