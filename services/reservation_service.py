from datetime import datetime
from database import db
from models.reservation_model import Reservation
from utils.validators import validate_reservation_data
import random
import string

PRICE_PER_ROOM = 3000  # KES

def calculate_total_amount(check_in_date, check_out_date, number_of_rooms):
    check_in = datetime.strptime(check_in_date, "%Y-%m-%d")
    check_out = datetime.strptime(check_out_date, "%Y-%m-%d")

    nights = (check_out - check_in).days

    total = nights * number_of_rooms * PRICE_PER_ROOM

    return total, nights

def generate_reservation_id():
    random_part = ''.join(
        random.choices(string.ascii_uppercase + string.digits, k=5)
    )
    return f"BLR-{random_part}"

def create_reservation(data):
    validation_error = validate_reservation_data(data)

    if validation_error:
        return validation_error, 400
    
    total_amount, nights = calculate_total_amount(
    data["check_in_date"],
    data["check_out_date"],
    int(data["number_of_rooms"]))

    reservation = Reservation(
        reservation_id=generate_reservation_id(),
        hotel_name=data["hotel_name"],
        number_of_rooms=int(data["number_of_rooms"]),
        check_in_date=data["check_in_date"],
        check_out_date=data["check_out_date"],
        customer_name=data["customer_name"],
        request_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        status="Confirmed",
        total_amount=total_amount,
        nights=nights
      
)
    db.session.add(reservation)   
    db.session.commit()

    return {
        "message": "Reservation created successfully",
        "reservation": reservation.to_dict(),
        "billing": {
            "price_per_room": PRICE_PER_ROOM,
            "nights": nights,
            "rooms": int(data["number_of_rooms"]),
            "total_amount": total_amount
        }
    }, 201


def get_all_reservations():
    reservations = Reservation.query.all()
 
    return {
        "total_reservations": len(reservations),
        "reservations": [reservation.to_dict() for reservation in reservations]
     }, 200