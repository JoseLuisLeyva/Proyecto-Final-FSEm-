// ##################################################
//
// Autor: Cortez Ibarra Derek 
//        Leyva Pérez José Luis
//        Muñoz Garcia Arturo
// License: MIT
//
// ##################################################
//Envia a base de datos
function valorVentilador(input,id_child,value) {
    $(id_child).html(value);
    setStorage('potenciaVentiladorActualizada',value); //guardamos en el localStorage, si te sales y entras esta el valor dado
    printLabel('spanpotenciaVentiladorActualizada',value);
     //Guardando en la base de datos
     valoresBD('potenciaVentiladorActualizadaa',value);
}