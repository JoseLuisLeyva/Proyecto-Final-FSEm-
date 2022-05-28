// ##################################################
//
// Autor: Cortez Ibarra Derek 
//        Leyva Pérez José Luis
//        Muñoz Garcia Arturo
// License: MIT
//
// ##################################################

function sendProgramarIrrigacion(botonProgramarIrrigacion){
    var controlInputIrrigacionInicial = getById ('inputProgramacionIrrigacionInicial');
    let horaIndicadaIrrigacionInicial = controlInputIrrigacionInicial.value;

    var controlInputIrrigacionFinal = getById ('inputProgramacionIrrigacionFinal');
    let horaIndicadaIrrigacionFinal = controlInputIrrigacionFinal.value;
    var controlSelect = getById('selectStatusIrrigacion');
    let statusIrrigacion = controlSelect.value;
    let statusIrrigacionStr = controlSelect.options[statusIrrigacion].text;
    
    let horaSistema = getById('HoraActual');
    myDate = new Date();
    
    if (!confirm('Se eligio como hora inicial  ' + horaIndicadaIrrigacionInicial + 'y como hora final  ' + horaIndicadaIrrigacionFinal+' ¿Esta seguro de que las horas son correctas?')){
        return;
    }
    
    setStorage('HoraIndicadaIrrigacionFinal',horaIndicadaIrrigacionFinal);
    setStorage('HoraIndicadaIrrigacionInicial',horaIndicadaIrrigacionInicial);

    valoresBD('HoraIndicadaIrrigacionFinal',horaIndicadaIrrigacionFinal);
    valoresBD('HoraIndicadaIrrigacionInicial',horaIndicadaIrrigacionInicial);
    programarIrrigacion(horaIndicadaIrrigacionInicial,horaIndicadaIrrigacionFinal);
}

