"""Невеликі перевірки вхідних даних, спільні для кількох ендпоінтів."""

from fastapi import HTTPException


def clean_name(value: str) -> str:
    """Прибирає зайві пробіли по краях і не дозволяє порожню назву."""
    name = value.strip()
    if not name:
        raise HTTPException(status_code=422, detail="Назва не може бути порожньою")
    return name
