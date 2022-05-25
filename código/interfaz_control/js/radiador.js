// ##################################################
//
// Autor: Cortez Ibarra Derek 
//        Leyva Pérez José Luis
//        Muñoz Garcia Arturo
// License: MIT
//
// ##################################################
//Envia los datos a la base de datos
function change_value_radiador(input,id_child,value) {
    $(id_child).html(value);
    setStorage('potenciaRadiadorNueva',value); //guardamos en el localStorage, si te sales y entras esta el valor dado
    printLabel('spanPotenciaRadiadorNueva',value); 

    valoresBD('potenciaRadiadorNueva',value);
}
