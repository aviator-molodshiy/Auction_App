# print("--- Детальний опис контейнера ---")
#
# # Створюємо порожній словник
# inventory = {}
#
# print("Вводьте дані про речі (для завершення введіть 'stop' у назві):")
#
# while True:
#     item_name = input("Назва речі: ")
#     if item_name.lower() == 'stop':
#         break
#
#     item_price = float(input(f"Ціна для '{item_name}' ($): "))
#
#     # Додаємо в словник: ключ — назва, значення — ціна
#     inventory[item_name] = item_price
#
# print("-" * 30)
# print("ВАШ ЗВІТ ПО КОНТЕЙНЕРУ:")
#
# total_value = 0
#
# # Перебираємо словник (назва та ціна)
# for name, price in inventory.items():
#     print(f"- {name}: ${price:.2f}")
#     total_value += price
#
# print("-" * 30)
# print(f"Загальна кількість унікальних речей: {len(inventory)}")
# print(f"Загальна вартість: ${total_value:.2f}")
#
# # --- ЗАПИС У ФАЙЛ ---
# file_name = "container_report.txt"
#
# # Відкриваємо файл для запису ('w' означає write)
# with open(file_name, "w", encoding="utf-8") as file:
#     file.write("--- ЗВІТ ПО КОНТЕЙНЕРУ ---\n")
#
#     for name, price in inventory.items():
#         file.write(f"- {name}: ${price:.2f}\n")
#
#     file.write("-" * 25 + "\n")
#     file.write(f"Загальна вартість: ${total_value:.2f}\n")
#
# print(f"\n✅ Звіт успішно збережено у файл: {file_name}")
#
# print("-" * 30)
# search_item = input("Яку річ знайти у звіті? ")
#
# # Перевіряємо, чи є така назва у нашому словнику
# if search_item in inventory:
#     price = inventory[search_item]
#     print(f"✅ Знайдено! {search_item} коштує ${price:.2f}")
# else:
#     print(f"❌ На жаль, речі '{search_item}' немає в цьому контейнері.")



import os

file_name = "container_report.txt"
inventory = {}

# --- КРОК 1: ЧИТАННЯ ДАНИХ З ФАЙЛУ (якщо він існує) ---
if os.path.exists(file_name):
    load_choice = input(f"Знайдено файл '{file_name}'. Завантажити дані? (yes/no): ").lower()

    if load_choice == 'yes':
        with open(file_name, "r", encoding="utf-8") as file:
            for line in file:
                # Шукаємо рядки, які починаються з "- " (наші товари)
                if line.startswith("- "):
                    # Прибираємо "- " і розбиваємо рядок по символу ":"
                    parts = line.replace("- ", "").split(": $")
                    if len(parts) == 2:
                        name = parts[0].strip()
                        price = float(parts[1].strip())
                        inventory[name] = price
        print(f"✅ Завантажено {len(inventory)} речей.")

# --- КРОК 2: ДОДАВАННЯ НОВИХ РЕЧЕЙ (твій старий код) ---
print("\nВводьте нові речі (або 'stop' для завершення):")
while True:
    item_name = input("Назва речі: ")
    if item_name.lower() == 'stop':
        break
    item_price = float(input(f"Ціна для '{item_name}' ($): "))
    inventory[item_name] = item_price

# --- КРОК 3: РОЗРАХУНОК ТА ЗАПИС (оновлюємо суму) ---
total_value = sum(inventory.values())
print(f"\nЗагальна вартість інвентарю: ${total_value:.2f}")

with open(file_name, "w", encoding="utf-8") as file:
    file.write("--- ЗВІТ ПО КОНТЕЙНЕРУ ---\n")
    for name, price in inventory.items():
        file.write(f"- {name}: ${price:.2f}\n")
    file.write("-" * 25 + "\n")
    file.write(f"Загальна вартість: ${total_value:.2f}\n")

print(f"✅ Дані оновлено у файлі: {file_name}")
