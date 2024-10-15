import os
from flask import Flask
from flask_mailman import Mail
from flask_cors import CORS
from dotenv import load_dotenv
from flask_swagger_ui import get_swaggerui_blueprint
from .routes import config_routes

mail = Mail()

def create_app():
    app = Flask(__name__)
    CORS(app)
    load_dotenv() #carregar variáveis de ambiente.

    # Caminho para o arquivo YAML da API
    SWAGGER_URL = '/docs'
    API_URL = '/static/API.yaml'

    
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "Support-API"
    })
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)



    app.config["MAIL_USERNAME"] = os.getenv("MAIL_AUTH_USER")
    app.config["MAIL_PASSWORD"] = os.getenv("MAIL_AUTH_PASS")
    app.config["MAIL_DEFAULT_SENDER"] = os.getenv("MAIL_AUTH_USER")
    app.config["MAIL_SERVER"] = os.getenv("MAIL_HOST")
    app.config["MAIL_PORT"] = int(os.getenv("MAIL_PORT"))
    app.config["MAIL_USE_TLS"] = not os.getenv("MAIL_SECURE").lower() == "true"
    app.config["MAIL_USE_SSL"] = os.getenv("MAIL_SECURE").lower() == "true"


    mail.init_app(app)

    config_routes(app)

    return app
