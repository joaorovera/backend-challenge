const button = document.getElementById("Enviar");

function sendForm(event) {
    event.preventDefault();

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
                const errorM = document.getElementById("errorM");
                errorM.textContent = errorData.detail || 'Ocorreu um erro ao enviar a mensagem.';
                errorM.style.display = 'block'
                document.getElementById('success-message').style.display = 'none'; 
                throw new Error(errorData.detail || 'Ocorreu um erro ao enviar a mensagem.');
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
        const errorM = document.getElementById("errorM");
        errorM.textContent = 'Erro de sistema, tente novamente mais tarde.';
        errorM.style.display = 'block';
        document.getElementById('success-message').style.display = 'none';
    });

}

button.addEventListener("click", sendForm)