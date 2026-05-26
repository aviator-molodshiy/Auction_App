import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_NAME = os.path.join(BASE_DIR, "container_report.txt")


# 1. ФУНКЦІЯ РОЗРАХУНКУ ПОДАТКУ
def calculate_tax(profit, tax_rate=0.15):
    """Рахує суму податку від прибутку (15% за замовчуванням)"""
    if profit > 0:
        return profit * tax_rate
    return 0.0


# 2. ФУНКЦІЯ ДЛЯ БЕЗПЕЧНОГО ВВЕДЕННЯ ЧИСЕЛ (НОВА)
def get_safe_float(prompt_text):
    """Запитує введення у користувача, поки він не введе коректне число"""
    while True:
        try:
            value = float(input(prompt_text))
            return value  # Якщо перетворення успішне, повертаємо число і виходимо
        except ValueError:
            print("❌ Помилка! Будь ласка, введіть числове значення (наприклад: 400 або 12.50)")


# 3. ФУНКЦІЯ ДЛЯ ЗАВАНТАЖЕННЯ ДАНИХ
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


# 4. ФУНКЦІЯ ДЛЯ ЗБЕРЕЖЕННЯ ДАНИХ
def save_inventory(file_path, inventory, total_value, container_cost, tax, net_profit):
    """Записує інвентар та повний фінансовий звіт у файл"""
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("--- ПОВНИЙ ЗВІТ ПО КОНТЕЙНЕРУ ---\n")
        for name, price in inventory.items():
            file.write(f"- {name}: ${price:.2f}\n")
        file.write("-" * 35 + "\n")
        file.write(f"Загальна вартість речей: ${total_value:.2f}\n")
        file.write(f"Витрати на купівлю лота: ${container_cost:.2f}\n")
        file.write(f"Податок США (15%): ${tax:.2f}\n")
        file.write(f"💰 ЧИСТИЙ ПРИБУТОК: ${net_profit:.2f}\n")

def find_expensive_items(inventory, min_price):
    result = {}
    for name, price in inventory.items():
        if price >= min_price:
            result[name] = price
    return result

# 5. ГОЛОВНА ФУНКЦІЯ ПРОГРАМИ
def main():
    print("--- Професійний Аукціон-Менеджер v2.5 (Захищений) ---")

    inventory = load_inventory(FILE_NAME)
    if inventory:
        print(f"🔄 Успішно завантажено {len(inventory)} речей з минулого звіту.")

    container_cost = get_safe_float("\nВведіть вартість купівлі цього контейнера ($): ")

    print("\n✍️ Вводьте нові речі (або 'stop' для завершення):")
    while True:
        item_name = input("Назва речі: ")
        if item_name.lower() == 'stop':
            break

        item_price = get_safe_float(f"Ціна для '{item_name}' ($): ")
        inventory[item_name] = item_price

    # Розрахунки
    total_value = sum(inventory.values())
    dirty_profit = total_value - container_cost

    tax_amount = calculate_tax(dirty_profit)
    net_profit = dirty_profit - tax_amount

    print("-" * 35)
    print(f"Загальна ринкова вартість речей: ${total_value:.2f}")
    print(f"Брудний прибуток (до податків): ${dirty_profit:.2f}")
    print(f"Податкові зобов'язання: ${tax_amount:.2f}")

    if net_profit > 0:
        print(f"🟢 ЧИСТИЙ ПРИБУТОК (після податків): ${net_profit:.2f} ✅")
    else:
        print(f"❌ Фінансовий збиток за цим лотом: ${abs(net_profit):.2f}")

    # --- НОВИЙ БЛОК ДЛЯ ДНЯ 11: ФІЛЬТРАЦІЯ РЕЧЕЙ < $500 ---
    print("-" * 35)
    print("🔍 Звіт по бюджетних лотах (Ціна < $500):")
    has_budget_items = False

    for name, price in inventory.items():
        if price < 500.0:
            print(f"  ↳ {name}: ${price:.2f}")
            has_budget_items = True

    if not has_budget_items:
        print("  Речей дешевше за $500 не знайдено.")
    print("-" * 35)


    # --- НОВИЙ БЛОК: ДОРОГІ РЕЧІ (ДОДАЙ ЦЕ) ---
    min_price_threshold = 1000  # межа для дорогих речей
    expensive = find_expensive_items(inventory, min_price_threshold)

    print(f"💎 Дорогі лоти (від ${min_price_threshold}):")
    if expensive:
        for name, price in expensive.items():
            print(f"  ↳ {name}: ${price:.2f}")
    else:
        print(f"  Речей дорожче за ${min_price_threshold} не знайдено.")
    print("-" * 35)


    save_inventory(FILE_NAME, inventory, total_value, container_cost, tax_amount, net_profit)
    print(f"\nПовний фінансовий аналіз збережено у файл.")


if __name__ == "__main__":
    main()