print("--- Розрахунок прибутку з контейнера ---")

# Отримуємо дані про витрати
container_price = float(input("Ціна контейнера на аукціоні ($): "))
clean_up_costs = float(input("Витрати на прибирання та вивіз ($): "))
storage_fee = float(input("Оренда складу для сортування ($): "))

# Отримуємо дані про очікуваний продаж
estimated_sales = float(input("Очікувана сума від продажу речей ($): "))

# Рахуємо результат
total_costs = container_price + clean_up_costs + storage_fee
profit = estimated_sales - total_costs

print("-" * 30)
print(f"Загальні витрати: ${total_costs}")

tax_rate = 0.15  # 15% податку

if profit > 0:
    net_profit = profit * (1 - tax_rate)
    print(f"✅ Очікуваний прибуток (брудними): ${profit}")
    print(f"💰 Чистий прибуток (після податків 15%): ${net_profit:.2f}")
    print("Порада: Це вигідна угода!")
elif profit == 0:
    print("⚠️ Ви вийдете в нуль.")
else:
    print(f"❌ Очікуваний збиток: ${abs(profit)}")
    print("Порада: Краще не купувати цей лот.")
