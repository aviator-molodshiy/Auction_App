# Auction Manager API

Backend-сервер для керування аукціонними контейнерами та речами.

## Стек технологій

- Python 3.14
- FastAPI - веб-фреймворк
- PostgreSQL - база даних
- SQLAlchemy - ORM для роботи з базою даних
- Uvicorn - ASGI-сервер

## Функціонал

- Отримання списку всіх контейнерів та речей
- Додавання нових речей у контейнери
- Автоматичне створення контейнера, якщо його не існує
- Збереження даних у PostgreSQL

## Як запустити

1. Клонувати репозиторій: git clone https://github.com/aviator-molodshiy/Auction_App.git
2. Встановити залежності: pip install fastapi uvicorn sqlalchemy psycopg2
3. Налаштувати PostgreSQL і створити базу auction_db
4. У файлі database.py вказати свій пароль PostgreSQL
5. Запустити сервер: uvicorn main:app --reload
6. Відкрити http://127.0.0.1:8000/docs

## API Ендпоінти

- GET / - Привітання
- GET /containers - Список усіх контейнерів
- POST /containers/{name}/items - Додати річ у контейнер

## Автор

Орест - https://github.com/aviator-molodshiy