// ##################################################
//
// Autor: Cortez Ibarra Derek 
//        Leyva Pérez José Luis
//        Muñoz Garcia Arturo
// License: MIT
//
// ##################################################

//Envia los datos a la base de datos
function change_value_Temperatura(input, id_child,value,sobreescribir) {
    $(id_child).html(value);
    //sobreescribir va a ser verdadero cuando le mueve el usurio
    // es falso cuando este haciendo la comparacion
    if (sobreescribir){
        guardarRespaldo('temperaturaNuevaBackup',value,sobreescribir);
    }
    setStorage('temperaturaNueva',value); //guardamos en el localStorage, si te sales y entras esta el valor dado
    printLabel('spanTemperaturaNueva',value);

    let valorTemperatura = parseInt(value); //garantizamos un valor entero

    //Guardando en la base de datos
    valoresBD('temperaturaInicial',valorTemperatura);

    
 
}

