from datetime import datetime

def validate_reservation_data(data):
    required_fields = [
        "hotel_name",
        "number_of_rooms",
        "check_in_date",
        "check_out_date",
        "customer_name"
    ]

    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        return {
            "error": "Missing required fields",
            "missing_fields": missing_fields
        }

    if data["hotel_name"] != "Blue Lagoon Hotels and Resorts":
        return {"error": "Invalid hotel name"}

    try:
        rooms = int(data["number_of_rooms"])

        if rooms <= 0:
            return {"error": "number_of_rooms must be greater than 0"}

    except (ValueError, TypeError):
        return {"error": "number_of_rooms must be an integer"}

    try:
        check_in = datetime.strptime(data["check_in_date"], "%Y-%m-%d")
        check_out = datetime.strptime(data["check_out_date"], "%Y-%m-%d")

        if check_out <= check_in:
            return {"error": "check_out_date must be later than check_in_date"}

    except ValueError:
        return {"error": "Dates must use YYYY-MM-DD format"}

    return None