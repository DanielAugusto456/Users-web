const txt_nombre = document.getElementById("txt_nombre");
const txt_contraseña = document.getElementById("txt_contraseña");
const btn_login = document.getElementById("btn_iniciar");
const btn_register = document.getElementById("btn_registrarse");

async function ReturnUsers() {
    try {
        const response = await fetch("./Data/users.json");
        const users = await response.json();
        return users;
        
    } catch (error) {
        alert("Error al obtener los usuarios: " + error);
        return [];
    }
}

btn_login.addEventListener("click", async () => {
    const users = await ReturnUsers();
    const name = txt_nombre.value;
    const password = txt_contraseña.value;
    let userFound = false;

    users.forEach(user => {
        if (name === user.nombre_completo && password === user.contrasena) {
            userFound = true;
            alert("Bienvenido " + user.nombre_completo);
            window.location.href = "dashboard.html";
        }
    });
    
    if (!userFound) {
        alert("Usuario o contraseña incorrectos");
    }
});

btn_register.addEventListener("click", () => {
    window.location.href = "user_register.html";
});