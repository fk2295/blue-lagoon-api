#from flask import Flask
#from routes.reservation_routes import reservation_bp

#app = Flask(__name__)
#app.register_blueprint(reservation_bp)

#if __name__ == "__main__":
    #app.run(debug=True)


import os
from flask import Flask
from config import Config
from database import db
from routes.reservation_routes import reservation_bp



app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(reservation_bp)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return {
        "message": "Blue Lagoon API is running",
        "endpoints": {
            "get_reservations": "/reservations",
            "create_reservation": "/reservations"
        }
    }, 200

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=True)
