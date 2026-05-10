print("--- Детальний опис контейнера ---")

# Створюємо порожній словник
inventory = {}

print("Вводьте дані про речі (для завершення введіть 'stop' у назві):")

while True:
    item_name = input("Назва речі: ")
    if item_name.lower() == 'stop':
        break

    item_price = float(input(f"Ціна для '{item_name}' ($): "))

    # Додаємо в словник: ключ — назва, значення — ціна
    inventory[item_name] = item_price

print("-" * 30)
print("ВАШ ЗВІТ ПО КОНТЕЙНЕРУ:")

total_value = 0

# Перебираємо словник (назва та ціна)
for name, price in inventory.items():
    print(f"- {name}: ${price:.2f}")
    total_value += price

print("-" * 30)
print(f"Загальна кількість унікальних речей: {len(inventory)}")
print(f"Загальна вартість: ${total_value:.2f}")
