from Python.services.note_service import NoteService

def route(app):

    @app.route("/mote", methods=["GET"])
    def make_note():
       return 200,  NoteService.make_note(request.json["url"], request.json["noteName"], request.json["noteContent"])
