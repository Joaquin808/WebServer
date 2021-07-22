from flask import request, jsonify

from services.login_service import LoginService


def route(app):

    @app.route("/login", methods=["GET"])
    def login():
        return jsonify(LoginService.check_login(request.json["username"], request.json["password"])), 200