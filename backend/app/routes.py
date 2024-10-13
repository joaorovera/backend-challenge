from .controller import process_ticket

def config_routes(app):
    @app.route("/ticket", methods=["POST"])
    def ticket_process():
        return process_ticket()

    @app.route("/teste")
    def teste():
        return "testando"

    