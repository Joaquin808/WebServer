from flask import render_template

def route(app):

    @app.route("/home", methods=["GET"])
    def home():
        return render_template("login.html")

    @app.route("/main", methods=["GET"])
    def main():
        return render_template("main.html")

    @app.route("/newNote", methods=["GET"])
    def note():
        return render_template("new_note.html")
