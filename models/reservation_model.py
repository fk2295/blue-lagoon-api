

from database import db

class Reservation(db.Model):
    __tablename__ = "reservations"

    id = db.Column(db.Integer, primary_key=True)
    reservation_id = db.Column(db.String(20), unique=True, nullable=False)
    hotel_name = db.Column(db.String(100), nullable=False)
    number_of_rooms = db.Column(db.Integer, nullable=False)
    check_in_date = db.Column(db.String(20), nullable=False)
    check_out_date = db.Column(db.String(20), nullable=False)
    customer_name = db.Column(db.String(100), nullable=False)
    request_time = db.Column(db.String(30), nullable=False)
    status = db.Column(db.String(20), nullable=False, default="Confirmed")
    total_amount = db.Column(db.Integer, nullable=False)
    nights = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "reservation_id": self.reservation_id,
            "hotel_name": self.hotel_name,
            "number_of_rooms": self.number_of_rooms,
            "check_in_date": self.check_in_date,
            "check_out_date": self.check_out_date,
            "customer_name": self.customer_name,
            "request_time": self.request_time,
            "status": self.status
        }