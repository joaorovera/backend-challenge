const button = document.getElementById("Enviar");

function sendForm(event) {
    event.preventDefault();
    console.log("Formulário enviado");

    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const message = document.getElementById("message").value;
    const captcha = grecaptcha.getresponse();

    const dados={
        name:name,
        email:email,
        comment:message,
        "g-recaptcha-response":captcha
    }

    let cabecalho={
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(dados)
    }

    fetch('http://localhost:5000/ticket', cabecalho)

    .then (response => {
        if (!response.ok) {
            const error = document.getElementById("error-message");
            error.textContent = 'Ocorreu um erro ao enviar a mensagem.'
            error.style.display = 'block'
            document.getElementById('success-message').style.display = 'none'; 
        }
        return response.json();
    })
    .then (dados =>{
        const success = document.getElementById("success-message");
        success.textContent = 'Mensagem enviada! De uma olhada em seu email.'
        success.style.display = 'block'
        document.getElementById('error-message').style.display = 'none';
    })
    .catch(error => {
        const errorMessage = document.getElementById("error-message");
        errorMessage.textContent = 'Erro de conexão. Tente novamente mais tarde.';
        errorMessage.style.display = 'block';
        document.getElementById('success-message').style.display = 'none';
    });

}

button.addEventListener("click", sendForm)