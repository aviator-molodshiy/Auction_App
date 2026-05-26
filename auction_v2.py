import json
import os



def add_item_to_container(containers_list):
    container_name = input("Назва контейнера (Container A / Container B): ")
    item_name = input("Назва речі: ")
    item_price = float(input("Ціна: $"))

    found = False

    for container in containers_list:
        if container['name'] == container_name:
            container['items'][item_name] = item_price
            print(f"{item_name} додано в {container_name} за ${item_price}")
            found = True

    if not found:
        print(f"Контейнер '{container_name}' не знайдено!")



def show_all_containers(containers_list):
    for container in containers_list:
        print(f"=== {container['name']} ===")
        for name, price in container['items'].items():
            print(f"{name}: ${price}")
        total = sum(container['items'].values())
        print(f"Загальна вартість: ${total}\n")



def save_to_file(containers_list, filename="auction_data.json"):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(base_dir, filename)


    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(containers_list, file, indent=4)
    print(f"Дані збережено у файл '{filename}'")



def load_from_file(filename="auction_data.json"):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(base_dir, filename)


    if not os.path.exists(filepath):
        print(f"Файл '{filepath}' не знайдено. Починаємо з порожнім списком.")
        return []

    with open(filepath, "r", encoding="utf-8") as file:
        containers_list = json.load(file)

    print(f"Завантажено {len(containers_list)} контейнерів із файлу.")
    return containers_list


if __name__ == "__main__":
    containers = load_from_file()


    if not containers:
        containers = [
        {"name": "Container A", "items": {"Chair": 100, "Table": 300}},
        {"name": "Container B", "items": {"Lamp": 50, "Vase": 80}}
        ]


    add_item_to_container(containers)
    show_all_containers(containers)
    save_to_file(containers)
