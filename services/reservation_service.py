from datetime import datetime
from database import db
from models.reservation_model import Reservation
from utils.validators import validate_reservation_data
import random
import string

def generate_reservation_id():
    random_part = ''.join(
        random.choices(string.ascii_uppercase + string.digits, k=5)
    )
    return f"BLR-{random_part}"

def create_reservation(data):
    validation_error = validate_reservation_data(data)

    if validation_error:
        return validation_error, 400

    reservation = Reservation(
        reservation_id=generate_reservation_id(),
        hotel_name=data["hotel_name"],
        number_of_rooms=int(data["number_of_rooms"]),
        check_in_date=data["check_in_date"],
        check_out_date=data["check_out_date"],
        customer_name=data["customer_name"],
        request_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        status="Confirmed"
    )

    db.session.add(reservation)   
    db.session.commit()

    return {
        "message": "Reservation created successfully",
        "reservation": reservation.to_dict()
    }, 201


def get_all_reservations():
    reservations = Reservation.query.all()
 
    return {
        "total_reservations": len(reservations),
        "reservations": [reservation.to_dict() for reservation in reservations]
     }, 200