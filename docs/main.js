document.addEventListener("DOMContentLoaded", function() {
    const loginForm = document.getElementById('login-form');
    if (loginForm) {
        loginForm.addEventListener('submit', function(e){
            e.preventDefault();
            const user = document.getElementById('username').value;
            const pass = document.getElementById('password').value;
            if(user === "admin" && pass === "Projekt2025"){
                window.location.href = "home.html";
            } else {
                alert("Benutzername oder Passwort falsch!");
            }
        });
    }

    const logoutForm = document.getElementById('logout-form');
    if (logoutForm) {
        logoutForm.addEventListener('submit', function(e){
            e.preventDefault();
            window.location.href = "start.html"; 
        });
    }

    const togglePassword = document.getElementById('toggle-password');
    const password = document.getElementById('password');

    togglePassword.addEventListener('click', function() {
        const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
        password.setAttribute('type', type);
        this.textContent = type === 'password' ? '👁️' : '🙈';
    });
});
