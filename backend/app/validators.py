from flask_mailman import EmailMessage
from flask import current_app
import re
import os
import requests


def check_email(content):
    standard = r"[^@]+@[^@]+\.[^@]+"
    mail = content.get("email")
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
    try:
        msg = EmailMessage(
            subject=os.getenv("TEXT_MAIL_TITLE"),
            body=os.getenv("TEXT_MAIL_BODY").format(email=content["email"], comment=content["comment"]),
            from_email=os.getenv("MAIL_AUTH_USER"),
            to=[os.getenv("MAIL_AUTH_USER")])

        msg2 = EmailMessage(
            subject=os.getenv("TEXT_MAIL_TITLE"),
            body=os.getenv("TEXT_MAIL_HTML").format(comment=content["comment"]),
            from_email=os.getenv("MAIL_AUTH_USER"),
            to=[os.getenv("DESTINY").format(email=content["email"])])
        
        msg.send()
        msg2.send()
        return False
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")
        return True
