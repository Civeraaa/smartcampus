from app.models import Room, RoomCreate, Booking, BookingCreate


class RoomService:
    def __init__(self):
        self.rooms: dict[int, Room] = {}
        self.next_id = 1

    def create_room(self, data: RoomCreate) -> Room:
        room = Room(id=self.next_id, **data.model_dump())
        self.rooms[self.next_id] = room
        self.next_id += 1
        return room

    def get_rooms(self) -> list[Room]:
        return list(self.rooms.values())

    def get_room(self, room_id: int) -> Room | None:
        return self.rooms.get(room_id)

    def delete_room(self, room_id: int) -> bool:
        if room_id not in self.rooms:
            return False

        del self.rooms[room_id]
        return True


room_service = RoomService()
class BookingService:
    def __init__(self):
        self.bookings: dict[int, Booking] = {}
        self.next_id = 1

    def create_booking(self, data: BookingCreate) -> Booking:
        # Comprobar que el aula existe
        if room_service.get_room(data.aula_id) is None:
            raise ValueError("Aula no encontrada")

        # Comprobar que la hora de inicio es anterior a la de fin
        if data.hora_inicio >= data.hora_fin:
            raise ValueError("La hora de inicio debe ser anterior a la hora de fin")

        # Comprobar que no hay reservas solapadas en esa aula y fecha
        for booking in self.bookings.values():
            if booking.aula_id == data.aula_id and booking.fecha == data.fecha:
                if (
                    data.hora_inicio < booking.hora_fin
                    and data.hora_fin > booking.hora_inicio
                ):
                    raise ValueError("La reserva se solapa con otra existente")

        booking = Booking(id=self.next_id, **data.model_dump())
        self.bookings[self.next_id] = booking
        self.next_id += 1
        return booking

    def get_bookings(self) -> list[Booking]:
        return list(self.bookings.values())

    def delete_booking(self, booking_id: int) -> bool:
        if booking_id not in self.bookings:
            return False

        del self.bookings[booking_id]
        return True


booking_service = BookingService()