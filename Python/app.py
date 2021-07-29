from flask import Flask
from flask_cors import CORS
from controllers import note_controller as nc, login_controller as lc, page_controller as pc
from flask import request

app = Flask(__name__)
pc.route(app)
nc.route(app)
lc.route(app)

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/shutdown', methods=['GET'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

CORS(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

