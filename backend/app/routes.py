from .controller import process_ticket

def route_teste(app):
    @app.route("/teste")
    def teste():
        return "<<<TESTANDO>>>"

def config_routes(app):
    @app.route("/ticket", methods=["POST"])
    def ticket_process():
        return process_ticket
    