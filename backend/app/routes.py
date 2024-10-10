from .controller import process_ticket
from flask import render_template

def config_routes(app):
    @app.route("/ticket", methods=["POST"])
    def ticket_process():
        return process_ticket
    
    @app.route("/")
    def home():
        return render_template("index.html")
    