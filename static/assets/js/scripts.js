let registroProducto = async () =>{

    let nombre      = document.getElementById("nombre").value;
    let primerApellido     = document.getElementById("primerApellido").value;
    let segundoApellido = document.getElementById("segundoApellido").value;
    let codigo = document.getElementById("codigo").value;
    let correo = document.getElementById("correo").value;
    let telefono = document.getElementById("telefono").value;
    let fecha = document.getElementById("fecha").value;
    
    const datos = new FormData();
    datos.append("nombre", nombre);
    datos.append("primerApellido", primerApellido);
    datos.append("segundoApellido" , segundoApellido);
    datos.append("codigo",codigo);
    datos.append("correo",correo);
    datos.append("telefono",telefono);  
    datos.append("fecha",fecha);  


    let respuesta  = await fetch('/registro',{
        method: 'POST',
        body: datos
    });
    let info = await respuesta.json();
    Swal.fire( 'Notificación', info.mensaje,'success');
    document.getElementById("nombre").value = "";
    document.getElementById("primerApellido").value ="";
    document.getElementById("segundoApellido").value="";
    document.getElementById("codigo").value="";
    document.getElementById("correo").value="";
    document.getElementById("telefono").value="";
    document.getElementById("fecha").value="";
}

//por aqui!!!!!!!!
let edicionProducto = async () =>{
    let url         = document.getElementById("frmEditar").action;

    let nombre      = document.getElementById("nombre").value;
    let primerApellido     = document.getElementById("primerApellido").value;
    let segundoApellido = document.getElementById("segundoApellido").value;
    let codigo = document.getElementById("codigo").value;
    let correo = document.getElementById("correo").value;
    let telefono = document.getElementById("telefono").value;
    let fecha = document.getElementById("fecha").value;
    
    const datos = new FormData();
    datos.append("nombre", nombre);
    datos.append("primerApellido", primerApellido);
    datos.append("segundoApellido" , segundoApellido);
    datos.append("codigo",codigo);
    datos.append("correo",correo);
    datos.append("telefono",telefono);  
    datos.append("fecha",fecha);  

    let respuesta  = await fetch(url, {
        method: 'POST',
        body: datos
    });
    let info = await respuesta.json();
    Swal.fire( 'Notificación', info.mensaje,'success');
}



// PENDIENTE: realizar el consumo del backend para la opcion de eliminar
let eliminar = async (id) => {
    let respuesta = await fetch('eliminar/' + id, {
        method: 'DELETE'
    });

    if (respuesta.ok) {
        Swal.fire('Notificación', 'El estudiante ha sido eliminado', 'success');
        document.getElementById("nombre").value = "";
        document.getElementById("primerApellido").value ="";
        document.getElementById("segundoApellido").value="";
        document.getElementById("codigo").value="";
        document.getElementById("correo").value="";
        document.getElementById("telefono").value="";
        document.getElementById("fecha").value="";
        
    } else {
        Swal.fire('Error', 'No se pudo eliminar el estudiante', 'error');
    }
}