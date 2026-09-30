# Hotel Management System (CLI)

A lightweight Python Command Line Interface (CLI) application built to streamline hotel front-desk operations, including room inventory registration, guest check-ins, automated stay billing, and room check-outs.

---

## Key Features

- **Room Cataloging**: Add and view hotel rooms with room numbers, room types (*Single*, *Double*, *Suite*), and price per night.
- **Occupancy Tracking**: Real-time status tracking (*Available* vs. *Occupied*) for all registered rooms.
- **Guest Check-In**: Assign guests to available rooms, set stay duration in nights, and generate total accommodation bills automatically.
- **Guest Check-Out**: Process guest departures and reset room availability flags instantly.
- **JSON Data Persistence**: Automatically loads and saves room and booking records into structured JSON files (`data/rooms.json` and `data/bookings.json`).

---

## Tech Stack

- **Language**: Python 3.8+
- **Libraries**: Built-in Python Standard Library (`datetime`, `json`, `os`, `sys`)
- **Storage**: JSON File Persistence

---

## Directory Structure

```text
hotel_management/
├── data/
│   ├── rooms.json
│   └── bookings.json
├── src/
│   ├── __init__.py
│   ├── models.py
│   ├── storage.py
│   ├── utils.py
│   └── hotel_service.py
├── main.py
├── README.md
├── statement.md
└── requirements.txt