from .controller import process_ticket
from flask import render_template, request

def config_routes(app):
    @app.route("/ticket", methods=["POST"])
    def ticket_process():
        return process_ticket()
    
    @app.route("/", methods=['GET', 'POST'])
    def home():
        if request.method == 'POST':
            return render_template("index.html") 
        return render_template("index.html") 

    