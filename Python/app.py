from flask import Flask
from flask_cors import CORS
from controllers import note_controller as nc, login_controller as lc

app = Flask(__name__)
nc.route(app)
lc.route(app)

CORS(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
