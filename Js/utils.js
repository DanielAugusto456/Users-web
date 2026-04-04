export async function ReturnUsers() {
    try {
        const response = await fetch("./Data/db.json");
        const data = await response.json();
        console.log("Usuarios obtenidos:", data.users);
        return data.users;
        
    } catch (error) {
        alert("Error al obtener los usuarios: " + error);
        return [];
    }
}

export async function SaveUser(newUser) {
    try {
        const respondse = await fetch("http://localhost:3000/users", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(newUser)
        });
        return result;

    } catch (error) {
       console.error("Error al guardar el usuario: " + error);
       return null; 
    }
}

export async function updateUser(id, updatedUser) {
    try {
        const response = await fetch(`http://localhost:3000/users/${id}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(updatedUser)
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const result = await response.json();
        console.log("Usuario actualizado:", result);
        return result;
    } catch (error) {
        console.error("Error al actualizar:", error);
        return null;
    }
}

export async function DeleteUser(id, userName) {
    // Confirmación nativa
    const confirmado = confirm(`¿Estás seguro de que deseas eliminar al usuario "${userName}"?`);
    
    if (!confirmado) {
        console.log("Eliminación cancelada");
        return false;
    }
    
    try {
        const response = await fetch(`http://localhost:3000/users/${id}`, {
            method: "DELETE"
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        console.log(`Usuario ${id} eliminado correctamente`);
        alert(`Usuario "${userName}" eliminado correctamente`);
        return true;
    } catch (error) {
        console.error("Error al eliminar usuario:", error);
        alert("Error al eliminar usuario: " + error.message);
        return false;
    }
}