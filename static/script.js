document.addEventListener('DOMContentLoaded', function () {
    console.log("JavaScript carregado com sucesso!");

    // Exemplo de animação ao enviar o formulário
    const contactForm = document.querySelector('form');
    if (contactForm) {
        contactForm.addEventListener('submit', function (event) {
            event.preventDefault(); // Previne o envio padrão do formulário
            alert("Seu formulário foi enviado com sucesso!");
        });
    }

    // Animação de scroll suave para links
    const links = document.querySelectorAll('a[href^="#"]');
    for (let link of links) {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    }
});
