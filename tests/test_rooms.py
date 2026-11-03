from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_room():
    response = client.post(
        "/rooms",
        json={
            "nombre": "Aula Test",
            "edificio": "A",
            "capacidad": 25,
            "equipamiento": ["ordenadores"]
        }
    )

    assert response.status_code == 201
    assert response.json()["nombre"] == "Aula Test"
    assert response.json()["capacidad"] == 25


def test_get_rooms():
    response = client.get("/rooms")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_room_by_id():
    create_response = client.post(
        "/rooms",
        json={
            "nombre": "Aula Individual",
            "edificio": "B",
            "capacidad": 15,
            "equipamiento": []
        }
    )
    room_id = create_response.json()["id"]

    response = client.get(f"/rooms/{room_id}")

    assert response.status_code == 200
    assert response.json()["id"] == room_id


def test_delete_room():
    create_response = client.post(
        "/rooms",
        json={
            "nombre": "Aula Para Borrar",
            "edificio": "C",
            "capacidad": 10,
            "equipamiento": []
        }
    )
    room_id = create_response.json()["id"]

    response = client.delete(f"/rooms/{room_id}")

    assert response.status_code == 200


def test_get_nonexistent_room():
    response = client.get("/rooms/99999")

    assert response.status_code == 404