// ##################################################
//
// Autor: Cortez Ibarra Derek 
//        Leyva Pérez José Luis
//        Muñoz Garcia Arturo
// License: MIT
//
// ##################################################

window.addEventListener("load",function(){

    
    //Carga del valor de la temperatura
    let temperaturaActualizada = getStorage('temperaturaNueva') == null ? 5 : getStorage('temperaturaNueva');
    let input = getById('temperaturaInicial');
    input.value=temperaturaActualizada;
    printLabel('spanTemperaturaNueva',temperaturaActualizada);
    

    //Carga el valor del ventilador
    let potenciaVentiladorActualizada = getStorage('potenciaVentiladorActualizada') == null ? 1200 : getStorage('potenciaVentiladorActualizada');
    let inputPotenciaVentilador = getById ('potenciaVentiladorInicial');
    inputPotenciaVentilador.value= potenciaVentiladorActualizada;
    printLabel('spanpotenciaVentiladorActualizada',potenciaVentiladorActualizada);

    //Carga el valor del radiador
    let potenciaRadiadorNueva = getStorage('potenciaRadiadorNueva') == null ? 1200 : getStorage('potenciaRadiadorNueva');
    let inputPotenciaRadiador= getById('potenciaRadiadorInicial');
    inputPotenciaRadiador.value=potenciaRadiadorNueva;
    printLabel('spanPotenciaRadiadorNueva',potenciaRadiadorNueva);

    //Carga estado de irigacion
    let statusIrrigacion =getStorage('StatusIrrigacion'), controlStatusIrrigacion = getById('selectStatusIrrigacion');
    controlStatusIrrigacion.value = statusIrrigacion ;
    var index = controlStatusIrrigacion.value;


    var statusIrrigacionStr = "No Iniciado"

    if(index != "")
    {
         statusIrrigacionStr = controlStatusIrrigacion.options[statusIrrigacion].text;
        
    }
    printLabel('spanStatusIrrigacion',statusIrrigacionStr);

    //Programacion Temperatura 
    let horaInicioTemperatura = getStorage('HoraIndicadaInicial',horaFinalTemperatura = getStorage('HoraIndicadaFinal'));
    let inputInicial= getById('inputProgramacionTemperaturaInicial'), inputFinal= getById('inputProgramacionTemperaturaFinal');
    inputInicial.value=horaInicioTemperatura;
    inputFinal.value=horaFinalTemperatura;


    //Programacion Irrigacion
    let  horaInicioIrrigacion = getStorage('HoraIndicadaIrrigacionInicial'),horaFinalIrrigacion = getStorage('HoraIndicadaIrrigacionFinal');
    let inputIrrigacionInicial= getById('inputProgramacionIrrigacionInicial') , inputIrrigacionFinal= getById('inputProgramacionIrrigacionFinal');;
    inputIrrigacionInicial.value=horaInicioIrrigacion;
    inputIrrigacionFinal.value=horaFinalIrrigacion;
    
});

//pintamos el valor requerido en los campos de texto 
function printLabel (tag,cadena){
    var elemento = getById (tag);
    elemento.textContent = cadena;
}

//Esta funcion se encarga de traer del localStorage la variable correspoendiente, mediante su key
function getStorage (key){
    return localStorage.getItem(key) == null ? "" : localStorage.getItem(key);
}

//Esta funcion manda a guardar la varibale correspondiente al LocalStorage 
// con su key y el valor desiganado por el usuario
function setStorage (key,valor){
    localStorage.setItem(key,valor);
}

function getById (elemento){
    return document.getElementById(elemento);
}

function showTime(){
    myDate = new Date();
    hours = myDate.getHours();
    minutes = myDate.getMinutes();
    seconds = myDate.getSeconds();
    if (hours < 10) hours = 0 + hours;
    if (minutes < 10) minutes = "0" + minutes;
    if (seconds < 10) seconds = "0" + seconds;
    $("#HoraActual").text(hours+ ":" +minutes+ ":" +seconds);
    setTimeout("showTime()", 1000); 
}

var timerTemperatura; // funciona como variable global
var timerIrrigacion;

function programarTemperatura(horaInicio,horaFin){
    let intervalo = 1000; //va en milisegundos
    stopTimmer(timerTemperatura); //limpia el anterior, para borrar la hora programada anterior
    timerTemperatura = setInterval(ejecutarProgramacionTemperatura,intervalo,horaInicio,horaFin); //ejecuta cierta funcion cada intervalo de tiempo
}
function programarIrrigacion(horaInicioIrrigacion,horaFinIrrigacion){
    let intervaloIrrigacion = 1000; //va en milisegundos
    stopTimmer(timerIrrigacion); //limpia el anterior, para borrar la hora programada anterior
    timerIrrigacion = setInterval(ejecutarProgramacionIrrigacion,intervaloIrrigacion,horaInicioIrrigacion,horaFinIrrigacion); //ejecuta cierta funcion cada intervalo de tiempo
}

//funcion general
function stopTimmer(timer){
    clearInterval(timer);//limpia el anterior, para borrar la hora programada anterior
}

function ejecutarProgramacionTemperatura(horaInicio,horaFin){
    var ahora =new Date();
    var hora = ahora.getHours();
    var minutos = ahora.getMinutes();
    // convertir cadenas a partir de un split, separados en un arreglo de valores 
    // seprado por el split
    var valoresInicio = horaInicio.split(':');
    var horasInicio = parseInt(valoresInicio[0]);
    var minutosInicio= parseInt(valoresInicio[1]);

    var valoresFinal = horaFin.split(':');
    var horasFinal = parseInt(valoresFinal[0]);
    var minutosFinal = parseInt(valoresFinal[1]);

 
    //se compara la hora del sistema con los valores ya enteros
    if (hora >= horasInicio && hora<= horasFinal){
        if (minutos >= minutosInicio && minutos<= minutosFinal){
            var rango = getById('temperaturaInicial');
            rango.value = 20 ; // al darle . value forzamos que cambie a 20
            change_value_Temperatura (rango,'temperaturaNueva',20,false);

        }else{
            var rango = getById('temperaturaInicial');
            var rangoRespaldo = getStorage ('temperaturaNuevaBackup');// es la de respaldo
            rango.value = rangoRespaldo ; // al darle . value forzamos que cambie a 20
            change_value_Temperatura (rango,'temperaturaNueva',rangoRespaldo,true);
            stopTimmer(timerTemperatura);
            //el change value lo manda directo al firebase 
            // ya que se mando a llamar la funcion ya previamente programada
        }

    }
    
}

function guardarRespaldo (key,value,sobreescribir){
    if (sobreescribir ){
       setStorage (key,value);
    }
}

function ejecutarProgramacionIrrigacion(horaInicioIrrigacion,horaFinIrrigacion){
    var ahoraIrrigacion =new Date();
    var horaIrrigacion = ahoraIrrigacion.getHours();
    var minutosIrrigacion = ahoraIrrigacion.getMinutes();
    // convertir cadenas a partir de un split, separados en un arreglo de valores 
    // seprado por el split
    var valoresInicioIrrigacion= horaInicioIrrigacion.split(':');
    var horasInicioIrrigacion = parseInt(valoresInicioIrrigacion[0]);
    var minutosInicioIrrigacion= parseInt(valoresInicioIrrigacion[1]);

    var valoresFinalIrrigacion = horaFinIrrigacion.split(':');
    var horasFinalIrrigacion = parseInt(valoresFinalIrrigacion[0]);
    var minutosFinalIrrigacion = parseInt(valoresFinalIrrigacion[1]);

 
    //se compara la hora del sistema con los valores ya enteros
    if (horaIrrigacion >= horasInicioIrrigacion && horaIrrigacion<= horasFinalIrrigacion){
        if (minutosIrrigacion >= minutosInicioIrrigacion && minutosIrrigacion<= minutosFinalIrrigacion){
            var select = getById('selectStatusIrrigacion');
            console.log ('ejecutando');
            select.value = '1'; // al darle . value forzamos que cambie a 20
            var boton = getById('btnEnviarStatus');
            envioEstadoIrrigacion(boton);
            

        }else{
            var select = getById('selectStatusIrrigacion');
            select.value = '2';
            console.log ('apagando');
            // ya que se mando a llamar la funcion ya previamente programada
            var boton = getById('btnEnviarStatus');
            envioEstadoIrrigacion(boton);
            stopTimmer(timerIrrigacion);
        }

    }
    
}





