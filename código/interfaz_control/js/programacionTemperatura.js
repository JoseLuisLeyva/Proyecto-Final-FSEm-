// ##################################################
//
// Autor: Cortez Ibarra Derek 
//        Leyva Pérez José Luis
//        Muñoz Garcia Arturo
// License: MIT
//
// ##################################################

function sendProgramarTemperatura(botonProgramarTemperatura){
    var controlInputInicial = getById ('inputProgramacionTemperaturaInicial');
    let horaIndicadaInicial = controlInputInicial.value;

    var controlInputFinal = getById ('inputProgramacionTemperaturaFinal');
    let horaIndicadaFinal = controlInputFinal.value;

    if (!confirm('Se eligio como hora inicial  ' + horaIndicadaInicial + 'y como hora final  ' + horaIndicadaFinal+' ¿Esta seguro de que las horas son correctas?')){
        return;
    }
    console.log ('La hora inicial es:  ' + horaIndicadaInicial + ' la hora final es:  ' + horaIndicadaFinal);
    setStorage('HoraIndicadaFinal',horaIndicadaFinal);
    setStorage('HoraIndicadaInicial',horaIndicadaInicial);

    valoresBD('HoraIndicadaFinal',horaIndicadaFinal);
    valoresBD('HoraIndicadaInicial',horaIndicadaInicial);

    programarTemperatura (horaIndicadaInicial,horaIndicadaFinal);
}





