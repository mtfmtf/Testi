// main.js
document.getElementById('login-form').addEventListener('submit', function(e){
    e.preventDefault();
    const user = document.getElementById('username').value;
    const pass = document.getElementById('password').value;

    // Einfacher Check
    if(user === "admin" && pass === "1234"){
        window.location.href = "index.html";
    } else {
        alert("Benutzername oder Passwort falsch!");
    }
});
