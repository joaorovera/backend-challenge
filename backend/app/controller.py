from .validators import check_email, check_name, check_message, check_captcha, valid_token, send_email
from flask import jsonify, request

def process_ticket():
    content = request.get_json()
    if not request.is_json:
        retorno = ({
            "type": "about:blank",
            "title": "BadRequestError",
            "detail": "A requisação não foi enviada no formato JSON",
            "instance": "/ticket",
        })
        return jsonify(retorno), 400

    if check_captcha(content):
        retorno = ({
            "type": "about:blank",
            "title": "Unauthorized",
            "detail": "O Captcha não foi verificado -> Inválido.",
            "instance": "/ticket",
        })
        return jsonify(retorno), 401
    
    if check_message(content):
        retorno = ({ 
            "type": "about:blank",
            "title": "BadRequestError",
            "detail": "A mensagem deve ter entre 10 e 2000 caracteres.",
            "instance": "/ticket",
        })
        return jsonify(retorno), 400

    if check_email(content):
        retorno = ({
            "type": "about:blank",
            "title": "BadRequestError",
            "detail": "O email está vazio ou é inválido.",
            "instance": "/ticket",
        })
        return jsonify(retorno), 400
    
    if check_name(content):
        retorno = ({
            "type": "about:blank",
            "title": "BadRequestError",
            "detail": "O nome precisa conter mais de 2 caracteres.",
            "instance": "/ticket",
        })
        return jsonify(retorno), 400

    if send_email(content):
        retorno = ({
            "type": "about:blank",
            "title": "InternalError",
            "detail": "O email não foi enviado de forma correta.",
            "instance": "/ticket",
        })
        return jsonify(retorno), 500

    return jsonify(content), 201
