import sys
from src.hotel_service import HotelService

def main():
    service = HotelService()

    while True:
        print("\n========================================")
        print("    HOTEL MANAGEMENT SYSTEM (CLI)")
        print("========================================")
        print("1. Add New Room")
        print("2. View All Rooms")
        print("3. Check-In Guest")
        print("4. Check-Out Guest")
        print("5. Exit")
        print("========================================")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            r_num = input("Enter Room Number: ").strip()
            r_type = input("Enter Room Type (Single/Double/Suite): ").strip()
            price = input("Enter Price Per Night (₹): ").strip()
            try:
                success, msg = service.add_room(r_num, r_type, float(price))
                print(f"\nResult: {msg}")
            except ValueError:
                print("\nError: Invalid price entered.")

        elif choice == "2":
            rooms = service.get_all_rooms()
            print("\n---------------- ROOM LIST ----------------")
            if not rooms:
                print("No rooms registered in the system.")
            for r in rooms:
                status = "Occupied" if r.is_occupied else "Available"
                print(f"Room [{r.room_number}] | Type: {r.room_type} | Price: ₹{r.price_per_night}/night | Status: {status}")

        elif choice == "3":
            b_id = input("Enter Booking ID: ").strip()
            g_name = input("Enter Guest Name: ").strip()
            r_num = input("Enter Room Number: ").strip()
            nights = input("Enter Number of Nights: ").strip()
            try:
                success, msg = service.check_in_guest(b_id, g_name, r_num, int(nights))
                print(f"\nResult: {msg}")
            except ValueError:
                print("\nError: Please enter valid numbers for nights.")

        elif choice == "4":
            r_num = input("Enter Room Number to Check-Out: ").strip()
            success, msg = service.check_out_guest(r_num)
            print(f"\nResult: {msg}")

        elif choice == "5":
            print("\nExiting Hotel Management System. Goodbye!")
            sys.exit(0)

        else:
            print("\nInvalid choice! Please select an option between 1 and 5.")

if __name__ == "__main__":
    main()