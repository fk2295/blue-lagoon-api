# Blue Lagoon Hotel Reservation API

A RESTful Flask web service for making hotel reservations at Blue Lagoon Hotels and Resorts.

## Features

- Create hotel reservation
- View all reservations
- JSON request and response
- SQLite database
- Simple reservation ID generation

## Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- Postman for testing

## Run Locally

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py


## API Endpoints
Create Reservations

POST /reservations

</> JSON
{
  "hotel_name": "Blue Lagoon Hotels and Resorts",
  "number_of_rooms": 2,
  "check_in_date": "2026-05-10",
  "check_out_date": "2026-05-12",
  "customer_name": "John Mwangi"
}


Get Reservations

GET /reservations
