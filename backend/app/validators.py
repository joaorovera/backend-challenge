from flask_mailman import EmailMessage
from flask_mail import Mail
import re
import os
import requests

email = Mail()

def check_email(content):
    standard = r"[^@]+@[^@]+\.[^@]+"
    mail = content.get("mail")
    return not re.match(standard, mail)

def check_name(content):
    name = content.get("name")
    if len(name) >= 2:
        return False
    return True

def check_message(content):
    msg = content.get("comment")
    return not (10<= len(msg) <= 2000)

def check_captcha(content):
    if "g-recaptcha-response" in content:
        captcha = content["g-recaptcha-response"]
        if valid_token(captcha):
            return False
    return True


def valid_token(token):
    url = os.getenv("RECAPTCHA_URL")
    secret = os.getenv("RECAPTCHA_SECRET")
    payload = {"secret": secret,
               "response": token
    }
    response = requests.post(url, data=payload)
    result = response.json()
    if "success" in result:
        resultado = result["success"]
        if resultado == True:
            return True
        else:
            return False
    else:
        return False

def send_email(content):
    msg = EmailMessage(
    subject= os.getenv("TEXT_MAIL_TITLE"),
    body= os.getenv("TEXT_MAIL_BODY").format(name=content["name"], email=content["mail"], comment=content["comment"]),
    sender= os.getenv("MAIL_AUTH_USER"),
    receivers = [os.getenv("MAIL_AUTH_USER")],
    )
    try:
        msg.send()
        return "Email enviado"
    except Exception as e:
        print(e)
        return True