from flask import request, jsonify

from services.note_service import NoteService

from logging import Logger

def route(app):
    @app.route("/note", methods=["POST"])
    def make_note():
        Logger.info(request.json())
        file = NoteService.make_note(request.json["url"], request.json["noteName"], request.json["noteContent"])
        return jsonify(file), 200

    @app.route("/notes", methods=["GET"])
    def get_all_notes():
        return jsonify(NoteService.get_all_notes()), 200
