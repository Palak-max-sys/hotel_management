import json
import os
from src.models import Room, Booking

class StorageHandler:
    def __init__(self, rooms_file="data/rooms.json", bookings_file="data/bookings.json"):
        self.rooms_file = rooms_file
        self.bookings_file = bookings_file
        self._ensure_files()

    def _ensure_files(self):
        os.makedirs(os.path.dirname(self.rooms_file), exist_ok=True)
        if not os.path.exists(self.rooms_file):
            with open(self.rooms_file, 'w') as f:
                json.dump([], f)
        if not os.path.exists(self.bookings_file):
            with open(self.bookings_file, 'w') as f:
                json.dump([], f)

    def load_rooms(self):
        try:
            with open(self.rooms_file, 'r') as f:
                return [Room.from_dict(item) for item in json.load(f)]
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def save_rooms(self, rooms):
        with open(self.rooms_file, 'w') as f:
            json.dump([r.to_dict() for r in rooms], f, indent=4)

    def load_bookings(self):
        try:
            with open(self.bookings_file, 'r') as f:
                return [Booking.from_dict(item) for item in json.load(f)]
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def save_bookings(self, bookings):
        with open(self.bookings_file, 'w') as f:
            json.dump([b.to_dict() for b in bookings], f, indent=4)