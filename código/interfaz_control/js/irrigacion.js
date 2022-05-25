// ##################################################
//
// Autor: Cortez Ibarra Derek 
//        Leyva Pérez José Luis
//        Muñoz Garcia Arturo
// License: MIT
//
// ##################################################
//Activa la irrigacion
function envioEstadoIrrigacion (btn) {
    var controlSelect = getById('selectStatusIrrigacion');
    // con var podemos modificar valores del elemento
    let statusIrrigacion = controlSelect.value;
    let statusIrrigacionStr = controlSelect.options[statusIrrigacion].text;


    setStorage('StatusIrrigacion',statusIrrigacion);
    printLabel('spanStatusIrrigacion',statusIrrigacionStr);


    valoresBD('StatusIrrigacion',statusIrrigacion);
    valoresBD('statusIrrigacionStr',statusIrrigacionStr);

}