# backend-challenge
O desafio propõe a implementação de um microserviço de um formulário de contato, que depois de ser preenchido, envie um email para a empresa que está utilizando o microserviço e uma cópia ao cliente, para que possa acompanhar o andamento via email.

## Índice

+ [Objetivo](#objetivo)
+ [Estrutura do Projeto](#estrutura-do-projeto)
+ [Tecnologias Utilizadas](#tecnologias-utilizadas)
+ [API](#API)
+ [Como Rodar](#como-rodar)

## Objetivo
Este projeto consiste em implementar um microserviço que irá gerenciar formulários de contato para a empresa e para o usuário. Sendo projetado para ser fácil de integrar

## Estrutura do Projeto

```plaintext
backend-challenge/
├── backend/
│   ├── app/
│   |   ├── __init__.py
│   |   ├── controller.py
│   |   ├── routes.py
│   |   ├── validators.py
│   ├── run.py
│   └── dockerfile
├── frontend/
│   ├── imagens/
│   ├── docker-compose.yml
│   └── dockerfile
│   ├── index.html
│   ├── scripts.js
│   ├── styles.css
└── README.md
```
## Tecnologias Utilizadas
<table>
    <tr>
        <td>Python</td>
        <td>flaskAPI</td>
        <td>HTML5</td>
        <td>docker</td>
        <td>Nginx</td>
    </tr>
    <tr>
        <td>Backend</td>
        <td>Backend</td>
        <td>Frontend</td>
        <td>Outras</td>
        <td>Outras</td>
    </tr>
</table>


## Como Rodar
Você terá que rodar localmente o front e o backend separadamente, para isso:

### Requisito

- Docker ⚠

### Passo a passo

1) Clonar o repositório:
    ```sh
    git clone https://github.com/joaorovera/backend-challenge.git
    cd backend-challenge
    ```

2) Faça o biuld do backend em um terminal:
    ```sh
    cd backend
    docker build -t backend .
    docker run -p 5000:5000 backend
    ```

3) Faça o biuld do frontend em outro terminal:
    ```sh
    cd frontend
    docker build -t frontend .
    docker run -p 80:80 frontend
    ```
4. Após isso, com os dois terminais já rodando nas portas epecificadas, acesse [localhost](http://localhost:80)

   Atenção: O Captcha funciona apenas em http://localhost:80.

## API

Se você quiser ver apenas a api, o arquivo API.yaml tem toda a documentação, de como deve responder e o que espera receber de parametros. Além disso o conteudo pode ser usado em um editor swagger.
