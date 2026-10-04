inventory = {
    "T-shirt": 60,
    "shoes": 80,
    "jeans": 70
}

print(sum(inventory.values()))

def show_inventory(items):
    print("--- Інвентар ---")
    for name, price in items.items():
        print(f"{name}: {price}")


def add_item(inv):
    name = input("Назва нової речі: ")
    price = float(input("Ціна: $"))
    inv[name] = price
    print(f" {name} додано за ${price}")

show_inventory(inventory)

add_item(inventory)


while True:
    search_item = input("Яку річ ви шукаєте? (або 'exit' для виходу): ")
    if search_item == "exit":
        print("До побачення!")
        break
    if search_item in inventory:
        print(f"Price: {inventory[search_item]} $")
    else:
        print("Not found")


