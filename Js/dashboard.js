import { ReturnUsers, SaveUser, updateUser, DeleteUser} from "../Js/utils.js";

const txt_name = document.getElementById("txt_name");
const txt_email = document.getElementById("txt_email");
const txt_password = document.getElementById("txt_password");
const txt_confirm_password = document.getElementById("txt_confirm_password");
const btn_save = document.getElementById("btn_save");
const user_list = document.getElementById("user_list");
const btn_search = document.getElementById("btn_search");
const txt_search = document.getElementById("txt_search");
let actual_id = null;

// evneto para los botones de actualizar
function asignarEventosUpdate() {
    document.querySelectorAll('.button-update').forEach(button => {
        // Remover eventos anteriores para evitar duplicados
        button.removeEventListener('click', handleUpdate);
        button.addEventListener('click', handleUpdate);
    });
}

function handleUpdate(event) {
    const button = event.currentTarget;
    const userName = button.getAttribute('data-name');
    const userEmail = button.getAttribute('data-email');
    const userPassword = button.getAttribute('data-password');
    actual_id = button.getAttribute('data-id');

    txt_name.value = userName || '';
    txt_email.value = userEmail || '';
    txt_password.value = userPassword || '';
    
    alert(`Editando usuario: ${userName}`);
}

// evento para los botones de eliminar
function asignarEventosDelete() {
    document.querySelectorAll('.button-delete').forEach(button => {
        button.removeEventListener('click', handleDelete);
        button.addEventListener('click', handleDelete);
    });
}

function handleDelete(event) {
    const button = event.currentTarget;
    const userId = button.getAttribute('data-id');
    const userName = button.getAttribute('data-name');
    
    DeleteUser(userId, userName);
    window.location.href = "dashboard.html";
}

function displayUsers(users) {
    user_list.innerHTML = "";
    users.forEach(user => {
        user_list.innerHTML += ` <div class="user-item p-4" data-user-id=${user.id} data-user-name=${user.nombre_completo} data-user-email=${user.correo_electronico}>
                <div class="user-name is-size-5">${user.nombre_completo}</div>
                <div class="user-email mt-1">${user.correo_electronico}</div>
                <div class="action-buttons mt-2">
                    <button class="button-update button is-small"
                            data-id=${user.id} 
                            data-password=${user.contrasena} 
                            data-name=${user.nombre_completo} 
                            data-email=${user.correo_electronico}>
                    Actualizar
                    </button>
                    <button class="button-delete button is-small" 
                            data-id="${user.id}"
                            data-name="${user.nombre_completo}">
                    Borrar
                    </button>
                </div>
            </div>`;
    });
    asignarEventosUpdate();
    asignarEventosDelete();
}

// funcion de busqueda de usuarios
btn_search.addEventListener("click", async () => {
    const users = await ReturnUsers();
    console.log("Usuarios obtenidos para búsqueda:", users);

    const searchTerm = txt_search.value.toLowerCase();
    const filteredUsers = users.filter(user =>
        user.nombre_completo.toLowerCase().includes(searchTerm) ||
        user.correo_electronico.toLowerCase().includes(searchTerm)
    );
    displayUsers(filteredUsers);
});

function ValidateTextsFields() {
    if (txt_name.value != "" && txt_email.value != "" && txt_password.value != "" && txt_confirm_password.value != "") {
        return true;
    }
    else {
        alert("Por favor, complete todos los campos.");
        return false;
    }
}

btn_save.addEventListener("click", async () => {
    if (actual_id != null) {
        if (ValidateTextsFields()) {
            if (txt_password.value === txt_confirm_password.value) {
                console.log("Actualizando usuario...");
                    let usuario = {
                        nombre_completo: txt_name.value,
                        correo_electronico: txt_email.value,
                        contrasena: txt_password.value
                    }
                updateUser(actual_id, usuario);
                alert("Usuario actualizado exitosamente.");
                window.location.href = "dashboard.html";
            }
            else{
                alert("Las contraseñas no coinciden.");
            }
        }
    }
    else {
        if (ValidateTextsFields()) {
            let usuario = {
                nombre_completo: txt_name.value,
                correo_electronico: txt_email.value,
                contrasena: txt_password.value
            }
            SaveUser(usuario);
            alert("Usuario registrado exitosamente.");
            window.location.href = "dashboard.html";
        }
    }
});