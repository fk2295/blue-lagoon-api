#from flask import Blueprint, request, jsonify
#from services.reservation_service import create_reservation, get_all_reservations
#from datetime import datetime
#from database import db
#from models.reservation_model import Reservation
#from utils.validators import validate_reservation_data

#reservation_bp = Blueprint("reservation_bp", __name__)

#@reservation_bp.route("/reservations", methods=["POST"])
#def make_reservation():
    #if not request.is_json:
        #return jsonify({"error": "Content-Type must be application/json"}), 400

    #data = request.get_json()
    #result, status_code = create_reservation(data)
    #return jsonify(result), status_code

#@reservation_bp.route("/reservations", methods=["GET"])
#def fetch_reservations():
    #result, status_code = get_all_reservations()
    #return jsonify(result), status_code


from flask import Blueprint, request, jsonify
from services.reservation_service import create_reservation, get_all_reservations

reservation_bp = Blueprint("reservation_bp", __name__)

@reservation_bp.route("/reservations", methods=["POST"])
def make_reservation():
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json"}), 400

    data = request.get_json()

    result, status_code = create_reservation(data)

    return jsonify(result), status_code


@reservation_bp.route("/reservations", methods=["GET"])
def fetch_reservations():
    result, status_code = get_all_reservations()

    return jsonify(result), status_code