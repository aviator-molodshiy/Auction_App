import json

products = {
    "Laptop": 700,
    "Mouse": 50,
    "keyboard": 120
}

json_string = json.dumps(products)
print("JSON-line:", json_string)


data = json.loads(json_string)
print("Назва товарів:", list(data.keys()))
