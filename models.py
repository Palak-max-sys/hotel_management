class Room:
    def __init__(self, room_number, room_type, price_per_night, is_occupied=False):
        self.room_number = str(room_number)
        self.room_type = room_type  # Single, Double, Suite
        self.price_per_night = float(price_per_night)
        self.is_occupied = is_occupied

    def to_dict(self):
        return {
            "room_number": self.room_number,
            "room_type": self.room_type,
            "price_per_night": self.price_per_night,
            "is_occupied": self.is_occupied
        }

    @staticmethod
    def from_dict(data):
        return Room(
            data["room_number"],
            data["room_type"],
            data["price_per_night"],
            data.get("is_occupied", False)
        )

class Booking:
    def __init__(self, booking_id, guest_name, room_number, nights, total_cost, check_in_date):
        self.booking_id = str(booking_id)
        self.guest_name = guest_name
        self.room_number = str(room_number)
        self.nights = int(nights)
        self.total_cost = float(total_cost)
        self.check_in_date = check_in_date

    def to_dict(self):
        return {
            "booking_id": self.booking_id,
            "guest_name": self.guest_name,
            "room_number": self.room_number,
            "nights": self.nights,
            "total_cost": self.total_cost,
            "check_in_date": self.check_in_date
        }

    @staticmethod
    def from_dict(data):
        return Booking(
            data["booking_id"],
            data["guest_name"],
            data["room_number"],
            data["nights"],
            data["total_cost"],
            data["check_in_date"]
        )