from .controller import process_ticket

def route_teste(app):
    @app.routes("/teste")
    def teste():
        return "<<<TESTANDO>>>"

def config_routes(app):
    @app.routes("/ticket", methods=["POST"])
    def ticket_process():
        return process_ticket
    