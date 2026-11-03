from fastapi import FastAPI, HTTPException
from app.models import RoomCreate, Room, BookingCreate, Booking
from app.services import room_service, booking_service

app = FastAPI(title="SmartCampus API")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/rooms", response_model=Room, status_code=201)
def create_room(data: RoomCreate):
    return room_service.create_room(data)


@app.get("/rooms", response_model=list[Room])
def get_rooms():
    return room_service.get_rooms()


@app.get("/rooms/{room_id}", response_model=Room)
def get_room(room_id: int):
    room = room_service.get_room(room_id)

    if room is None:
        raise HTTPException(status_code=404, detail="Aula no encontrada")

    return room


@app.delete("/rooms/{room_id}")
def delete_room(room_id: int):
    deleted = room_service.delete_room(room_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Aula no encontrada")

    return {"message": "Aula eliminada correctamente"}

@app.post("/bookings", response_model=Booking, status_code=201)
def create_booking(data: BookingCreate):
    try:
        return booking_service.create_booking(data)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@app.get("/bookings", response_model=list[Booking])
def get_bookings():
    return booking_service.get_bookings()


@app.delete("/bookings/{booking_id}")
def delete_booking(booking_id: int):
    deleted = booking_service.delete_booking(booking_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Reserva no encontrada")

    return {"message": "Reserva eliminada correctamente"}