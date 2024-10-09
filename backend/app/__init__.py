from flask import Flask
from flask_mail import Mail
from dotenv import load_dotenv
import os

email = Mail()

def create_app():
    app = Flask(__name__)
    load_dotenv() #carregar variáveis de ambiente.

    app.config["MAIL_SERVER"] = os.getenv("MAIL_HOST")
    app.config["MAIL_PORT"] = int(os.getenv("MAIL_PORT"))
    app.config["MAIL_USE_TLS"] = not os.getenv("MAIL_SECURE").lower() == True
    app.config["MAIL_USERNAME"] = os.getenv("MAIL_AUTH_USER")
    app.config["MAIL_PASSWORD"] = os.getenv("MAIL_AUTH_PASS")
    app.config["MAIL_DEFAULT_SENDER"] = os.getenv("MAIL_AUTH_USER")

    Mail.init_app(app)

    #aguardando a criação das rotas

    return app
