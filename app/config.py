"""Налаштування застосунку. Значення беруться зі змінних середовища або з файлу .env."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Обов'язкова змінна: адреса бази даних, наприклад
    # postgresql://користувач:пароль@localhost:5432/auction_db
    database_url: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
