// ##################################################
//
// Autor: Cortez Ibarra Derek 
//        Leyva Pérez José Luis
//        Muñoz Garcia Arturo
// License: MIT
//
// ##################################################

function valoresBD(key,valor){
    // URL base de datos/parametros/valor
    firebase.database().ref('valores/'+ key).set({
        value: valor
    });

}
