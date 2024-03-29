from flask import request, jsonify

from services.login_service import LoginService

from logging import Logger

def route(app):

    @app.route("/login", methods=["POST"])
    def login():
       #  start_response('201 OK', [('Content-Type', 'application/json',
       #  ('Access-Control-Allow-Headers','authorization'),
       #  ('Access-Control-Allow-Methods','HEAD, GET, POST, PUT, PATCH, DELETE'),
       #  ('Access-Control-Allow-Origin','*'),
       #  ('Access-Control-Max-Age','600'))])
        
       #  Logger.info(request.json())
        return jsonify(LoginService.check_login(request.json["username"], request.json["password"])), 200
