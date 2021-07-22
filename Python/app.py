from flask import Flask
from flask_cors import CORS
from controllers import note_controller as nc

app = Flask(__name__)
nc.route(app)

CORS(app)

if __name__ == "__main__":
    app.run()
