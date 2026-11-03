from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_booking():
    room_response = client.post(
        "/rooms",
        json={
            "nombre": "Aula Test",
            "edificio": "A",
            "capacidad": 20,
            "equipamiento": ["ordenadores"]
        }
    )
    room_id = room_response.json()["id"]

    response = client.post(
        "/bookings",
        json={
            "aula_id": room_id,
            "usuario": "Test",
            "fecha": "2026-11-10",
            "hora_inicio": "10:00:00",
            "hora_fin": "11:00:00"
        }
    )

    assert response.status_code == 201
    assert response.json()["aula_id"] == room_id


def test_booking_with_nonexistent_room():
    response = client.post(
        "/bookings",
        json={
            "aula_id": 9999,
            "usuario": "Test",
            "fecha": "2026-11-10",
            "hora_inicio": "10:00:00",
            "hora_fin": "11:00:00"
        }
    )

    assert response.status_code == 400


def test_overlapping_bookings():
    room_response = client.post(
        "/rooms",
        json={
            "nombre": "Aula Solapamiento",
            "edificio": "A",
            "capacidad": 20,
            "equipamiento": []
        }
    )
    room_id = room_response.json()["id"]

    booking_data = {
        "aula_id": room_id,
        "usuario": "Test",
        "fecha": "2026-11-11",
        "hora_inicio": "10:00:00",
        "hora_fin": "12:00:00"
    }

    first_response = client.post("/bookings", json=booking_data)
    assert first_response.status_code == 201

    overlapping_data = {
        **booking_data,
        "hora_inicio": "11:00:00",
        "hora_fin": "13:00:00"
    }

    second_response = client.post("/bookings", json=overlapping_data)
    assert second_response.status_code == 400