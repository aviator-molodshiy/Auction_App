import os

# Автоматично знаходимо шлях до головної папки проєкту, де лежить правильний звіт
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_NAME = os.path.join(BASE_DIR, "container_report.txt")


# 1. ФУНКЦІЯ РОЗРАХУНКУ ПОДАТКУ
def calculate_tax(profit, tax_rate=0.15):
    """Рахує суму податку від прибутку"""
    if profit > 0:
        return profit * tax_rate
    return 0.0


# 2. ФУНКЦІЯ ДЛЯ ЗАВАНТАЖЕННЯ ДАНИХ
def load_inventory(file_path):
    """Завантажує дані з текстового файлу в словник"""
    loaded_data = {}
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                if line.startswith("- "):
                    parts = line.replace("- ", "").split(": $")
                    if len(parts) == 2:
                        loaded_data[parts[0].strip()] = float(parts[1].strip())
    return loaded_data


# 3. ФУНКЦІЯ ДЛЯ ЗБЕРЕЖЕННЯ ДАНИХ
def save_inventory(file_path, inventory, total_value):
    """Записує поточний словник інвентарю у текстовий файл"""
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("--- ЗВІТ ПО КОНТЕЙНЕРУ ---\n")
        for name, price in inventory.items():
            file.write(f"- {name}: ${price:.2f}\n")
        file.write("-" * 25 + "\n")
        file.write(f"Загальна вартість: ${total_value:.2f}\n")


# 4. ГОЛОВНА ФУНКЦІЯ ПРОГРАМИ
def main():
    print("--- Професійний Аукціон-Менеджер ---")

    # Завантажуємо старі дані
    inventory = load_inventory(FILE_NAME)
    if inventory:
        print(f"✅ Успішно завантажено {len(inventory)} речей з минулого звіту.")
    else:
        print("ℹ️ Минулий звіт порожній або файл не знайдено. Починаємо новий облік.")

    print("\nВводьте нові речі (або 'stop' для завершення):")
    while True:
        item_name = input("Назва речі: ")
        if item_name.lower() == 'stop':
            break
        item_price = float(input(f"Ціна для '{item_name}' ($): "))
        inventory[item_name] = item_price

    total_value = sum(inventory.values())
    print(f"\nЗагальна вартість інвентарю: ${total_value:.2f}")

    # Викликаємо функцію збереження, щоб оновити файл на диску
    save_inventory(FILE_NAME, inventory, total_value)
    print(f"✅ Дані успішно оновлено та збережено у файлі.")


if __name__ == "__main__":
    main()
