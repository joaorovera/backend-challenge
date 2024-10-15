const button = document.getElementById("Enviar");

function sendForm(event) {
    event.preventDefault();
    console.log("Formulário enviado");

    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const message = document.getElementById("message").value;
    const captcha = grecaptcha.getResponse();

    const dados={
        name:name,
        email:email,
        comment:message,
        "g-recaptcha-response":captcha
    }


    fetch('http://127.0.0.1:5000/ticket', {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(dados)
    })

    .then (response => {
        if (!response.ok) {
            return response.json().then(errorData => {
                const error = document.getElementById("error-message");
                error.textContent = errorData.detail || 'Ocorreu um erro ao enviar a mensagem.';
                error.style.display = 'block'
                document.getElementById('success-message').style.display = 'none'; 
                throw new Error(data.detail || 'Ocorreu um erro ao enviar a mensagem.');
            });
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
        console.error('Erro:', error);
        const errorMessage = document.getElementById("error-message");
        errorMessage.textContent = 'Ocorreu um erro ao enviar a mensagem.';
        errorMessage.style.display = 'block';
        document.getElementById('success-message').style.display = 'none';
    });

}

button.addEventListener("click", sendForm)