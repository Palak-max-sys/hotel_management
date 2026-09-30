from src.models import Room, Booking
from src.storage import StorageHandler
from src.utils import get_current_date, calculate_total_bill

class HotelService:
    def __init__(self):
        self.storage = StorageHandler()
        self.rooms = self.storage.load_rooms()
        self.bookings = self.storage.load_bookings()

    def add_room(self, room_number, room_type, price_per_night):
        if any(r.room_number == str(room_number) for r in self.rooms):
            return False, "Room number already exists!"
        new_room = Room(room_number, room_type, price_per_night)
        self.rooms.append(new_room)
        self.storage.save_rooms(self.rooms)
        return True, f"Room {room_number} added successfully!"

    def get_all_rooms(self):
        return self.rooms

    def check_in_guest(self, booking_id, guest_name, room_number, nights):
        room = next((r for r in self.rooms if r.room_number == str(room_number)), None)
        if not room:
            return False, "Room not found!"
        if room.is_occupied:
            return False, "Room is currently occupied!"
        
        if any(b.booking_id == str(booking_id) for b in self.bookings):
            return False, "Booking ID already exists!"

        total_cost = calculate_total_bill(room.price_per_night, nights)
        check_in_date = get_current_date()

        new_booking = Booking(booking_id, guest_name, room_number, nights, total_cost, check_in_date)
        room.is_occupied = True

        self.bookings.append(new_booking)
        self.storage.save_rooms(self.rooms)
        self.storage.save_bookings(self.bookings)

        return True, f"Guest checked in successfully! Total Bill: ₹{total_cost}"

    def check_out_guest(self, room_number):
        room = next((r for r in self.rooms if r.room_number == str(room_number)), None)
        if not room or not room.is_occupied:
            return False, "Room is not currently occupied!"

        room.is_occupied = False
        self.storage.save_rooms(self.rooms)
        return True, f"Guest checked out from Room {room_number} successfully!"