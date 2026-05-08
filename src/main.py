print("--- Опис вмісту контейнера ---")

# Створюємо порожній список для цін речей
prices = []

print("Вводьте ціни речей (для завершення введіть 0):")

while True:
    price = float(input("Ціна речі ($): "))
    if price == 0:
        break  # Виходимо з циклу, якщо ввели 0
    prices.append(price)  # Додаємо ціну в наш список

# Рахуємо загальну суму всіх речей
total_value = sum(prices)
# Рахуємо кількість речей
items_count = len(prices)

print("-" * 30)
print(f"Всього знайдено речей: {items_count}")
print(f"Загальна вартість вмісту: ${total_value:.2f}")

if items_count > 0:
    average_price = total_value / items_count
    print(f"Середня ціна однієї речі: ${average_price:.2f}")
