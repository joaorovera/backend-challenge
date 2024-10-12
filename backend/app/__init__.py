import os
from flask import Flask, render_template
from flask_mail import Mail
from flask_cors import CORS
from dotenv import load_dotenv
from .routes import config_routes


def create_app():
    app = Flask(__name__)
    CORS(app)
    load_dotenv() #carregar variáveis de ambiente.



    app.config["MAIL_USERNAME"] = os.getenv("MAIL_AUTH_USER")
    app.config["MAIL_PASSWORD"] = os.getenv("MAIL_AUTH_PASS")
    app.config["MAIL_DEFAULT_SENDER"] = os.getenv("MAIL_AUTH_USER")
    app.config["MAIL_SERVER"] = os.getenv("MAIL_HOST")
    app.config["MAIL_PORT"] = int(os.getenv("MAIL_PORT"))
    app.config["MAIL_USE_TLS"] = not os.getenv("MAIL_SECURE").lower() == True


    email = Mail(app)

    config_routes(app)

    return app
