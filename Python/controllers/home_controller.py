from flask import render_template

def route(app):

    @app.route("/home", methods=["GET"])
    def home():
        return render_template("login.html")