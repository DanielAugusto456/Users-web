export async function ReturnUsers() {
    try {
        const response = await fetch("./Data/users.json");
        const data = await response.json();
        console.log("Usuarios obtenidos:", data.users);
        return data.users;
        
    } catch (error) {
        alert("Error al obtener los usuarios: " + error);
        return [];
    }
}

export function obtenerUltimoId(users) {
    if (users.length === 0) return 0;
    const ids = users.map(user => user.id);
    return Math.max(...ids);
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