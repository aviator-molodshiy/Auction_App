def create_item(client, container="Box", name="Лампа", price=10.0):
    response = client.post(
        f"/containers/{container}/items",
        params={"item_name": name, "item_price": price},
    )
    return response.json()


def test_list_items_returns_all_items(client):
    create_item(client, name="Лампа")
    create_item(client, container="Other", name="Стілець")

    response = client.get("/items")

    assert response.status_code == 200
    assert [item["name"] for item in response.json()] == ["Лампа", "Стілець"]


def test_get_item_by_id(client):
    item = create_item(client)

    response = client.get(f"/items/{item['id']}")

    assert response.status_code == 200
    assert response.json()["name"] == "Лампа"


def test_get_missing_item_returns_404(client):
    response = client.get("/items/999")

    assert response.status_code == 404


def test_patch_changes_only_sent_fields(client):
    item = create_item(client, name="Лампа", price=10.0)

    response = client.patch(f"/items/{item['id']}", params={"item_price": 25.0})

    assert response.status_code == 200
    assert response.json()["price"] == 25.0
    assert response.json()["name"] == "Лампа"


def test_patch_changes_name(client):
    item = create_item(client, name="Лампа", price=10.0)

    response = client.patch(f"/items/{item['id']}", params={"item_name": "Торшер"})

    assert response.json()["name"] == "Торшер"
    assert response.json()["price"] == 10.0


def test_patch_without_fields_changes_nothing(client):
    item = create_item(client)

    response = client.patch(f"/items/{item['id']}")

    assert response.status_code == 200
    assert response.json() == item


def test_patch_rejects_invalid_price(client):
    item = create_item(client)

    response = client.patch(f"/items/{item['id']}", params={"item_price": -1})

    assert response.status_code == 422


def test_patch_rejects_blank_name(client):
    item = create_item(client)

    response = client.patch(f"/items/{item['id']}", params={"item_name": "   "})

    assert response.status_code == 422


def test_patch_missing_item_returns_404(client):
    response = client.patch("/items/999", params={"item_price": 5})

    assert response.status_code == 404


def test_delete_item(client):
    item = create_item(client)

    response = client.delete(f"/items/{item['id']}")

    assert response.status_code == 204
    assert client.get(f"/items/{item['id']}").status_code == 404


def test_delete_missing_item_returns_404(client):
    response = client.delete("/items/999")

    assert response.status_code == 404
