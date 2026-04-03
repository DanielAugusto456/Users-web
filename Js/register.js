import { ReturnUsers, SaveUser} from "../Js/utils.js";

const txt_name = document.getElementById("txt_name");
const txt_email = document.getElementById("txt_email");
const txt_password = document.getElementById("txt_password");
const txt_confirm_password = document.getElementById("txt_confirm_password");
const btn_register = document.getElementById("btn_register");
const btn_exit = document.getElementById("btn_exit");

btn_register.addEventListener("click", () => {
    if (txt_name.value != "" && txt_email.value != "" && txt_password.value != "" && txt_confirm_password.value != "") {
        if (txt_password.value === txt_confirm_password.value) {
            console.log("Registrando usuario...");
            const usuario = {
                nombre_completo: txt_name.value,
                correo_electronico: txt_email.value,
                contrasena: txt_password.value
            }

            SaveUser(usuario)
            alert("Usuario registrado exitosamente.");
            window.location.href = "index.html";
        }
        else{
            alert("Las contraseñas no coinciden.");
        }
    }
    else{
        alert("Por favor, complete todos los campos.");
    }
});

btn_exit.addEventListener("click", () => {
    window.location.href = "index.html";
});