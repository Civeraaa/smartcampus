from app.models import RoomCreate, BookingCreate
from app.services import RoomService, BookingService


def test_room_service_create_and_get():
    service = RoomService()

    room = service.create_room(
        RoomCreate(
            nombre="Aula Servicio",
            edificio="A",
            capacidad=20,
            equipamiento=["ordenadores"]
        )
    )

    assert room.id == 1
    assert len(service.get_rooms()) == 1
    assert service.get_room(room.id) == room


def test_room_service_delete():
    service = RoomService()

    room = service.create_room(
        RoomCreate(
            nombre="Aula Borrar",
            edificio="B",
            capacidad=10,
            equipamiento=[]
        )
    )

    assert service.delete_room(room.id) is True
    assert service.get_room(room.id) is None
    assert service.delete_room(room.id) is False


def test_booking_service_create():
    room_service = RoomService()
    room = room_service.create_room(
        RoomCreate(
            nombre="Aula Reserva",
            edificio="A",
            capacidad=20,
            equipamiento=[]
        )
    )

    # BookingService usa room_service globalmente.
    from app import services
    services.room_service = room_service

    booking_service = BookingService()
    booking = booking_service.create_booking(
        BookingCreate(
            aula_id=room.id,
            usuario="Test",
            fecha="2026-11-12",
            hora_inicio="10:00:00",
            hora_fin="11:00:00"
        )
    )

    assert booking.id == 1
    assert booking.aula_id == room.id
    assert len(booking_service.get_bookings()) == 1