import pytest


def add_item(client, container="Box-1", name="Годинник", price=150.5):
    return client.post(
        f"/containers/{container}/items",
        params={"item_name": name, "item_price": price},
    )


def test_root_returns_message(client):
    response = client.get("/")

    assert response.status_code == 200
    assert "message" in response.json()


def test_health_check(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_add_item_creates_container_automatically(client):
    response = add_item(client)

    assert response.status_code == 201
    body = response.json()
    assert body["name"] == "Годинник"
    assert body["price"] == 150.5
    assert "id" in body

    container = client.get("/containers/Box-1")
    assert container.status_code == 200
    assert [item["name"] for item in container.json()["items"]] == ["Годинник"]


def test_add_item_to_existing_container_does_not_duplicate_it(client):
    add_item(client, name="Перша")
    add_item(client, name="Друга")

    containers = client.get("/containers").json()

    assert len(containers) == 1
    assert [item["name"] for item in containers[0]["items"]] == ["Перша", "Друга"]


def test_same_item_name_can_be_added_twice(client):
    add_item(client, name="Лампа")
    response = add_item(client, name="Лампа")

    assert response.status_code == 201
    assert len(client.get("/containers/Box-1").json()["items"]) == 2


@pytest.mark.parametrize("bad_price", [0, -5, "багато"])
def test_add_item_rejects_invalid_price(client, bad_price):
    response = add_item(client, price=bad_price)

    assert response.status_code == 422


@pytest.mark.parametrize("bad_name", ["", "   "])
def test_add_item_rejects_blank_name(client, bad_name):
    response = add_item(client, name=bad_name)

    assert response.status_code == 422


def test_blank_item_does_not_create_container(client):
    add_item(client, container="Empty-Box", name="   ")

    assert client.get("/containers/Empty-Box").status_code == 404


def test_add_item_strips_spaces_in_name(client):
    response = add_item(client, name="  Лампа  ")

    assert response.json()["name"] == "Лампа"


def test_create_container_returns_201(client):
    response = client.post("/containers", params={"name": "Box-2"})

    assert response.status_code == 201
    assert response.json()["name"] == "Box-2"
    assert response.json()["items"] == []


@pytest.mark.parametrize("bad_name", ["", "   "])
def test_create_container_rejects_blank_name(client, bad_name):
    response = client.post("/containers", params={"name": bad_name})

    assert response.status_code == 422


def test_create_duplicate_container_returns_409(client):
    client.post("/containers", params={"name": "Box-2"})

    response = client.post("/containers", params={"name": "Box-2"})

    assert response.status_code == 409


def test_get_missing_container_returns_404(client):
    response = client.get("/containers/unknown")

    assert response.status_code == 404


def test_delete_container_removes_its_items(client):
    item_id = add_item(client).json()["id"]

    response = client.delete("/containers/Box-1")

    assert response.status_code == 204
    assert client.get("/containers/Box-1").status_code == 404
    assert client.get(f"/items/{item_id}").status_code == 404


def test_delete_missing_container_returns_404(client):
    response = client.delete("/containers/unknown")

    assert response.status_code == 404


def test_containers_pagination(client):
    for number in range(5):
        client.post("/containers", params={"name": f"Box-{number}"})

    first_page = client.get("/containers", params={"limit": 2}).json()
    second_page = client.get("/containers", params={"skip": 2, "limit": 2}).json()

    assert [c["name"] for c in first_page] == ["Box-0", "Box-1"]
    assert [c["name"] for c in second_page] == ["Box-2", "Box-3"]


@pytest.mark.parametrize("params", [{"limit": 0}, {"limit": 1000}, {"skip": -1}])
def test_containers_pagination_rejects_bad_values(client, params):
    response = client.get("/containers", params=params)

    assert response.status_code == 422
