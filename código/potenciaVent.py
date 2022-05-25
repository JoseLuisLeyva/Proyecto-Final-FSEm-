#Ref: https://noctua.at/es/products/fan/nf-f12-pwm/specification
#https://solectroshop.com/es/blog/que-es-pwm-y-como-usarlo--n38
#potMax=0.6 W
#AmperajeMax=0.05 A
#voltaje Max=12 V
#Dutycycle=(Vpromedio*100)/(voltajeMax-voltajeMin)



import math


def valor_dutycycle(potencia):
    potenciaCalcular = int(potencia)/1000
    


    #PWM
    Amperaje=0.05
    volatajeMax=12
    VoltajeMin=0

    
    volataje=potenciaCalcular/Amperaje
    dutycycle=(volataje*100)/(volatajeMax-VoltajeMin)

    #Frecuencia Corte usamos un condensador pwm con una R=10k ohms y un capacitor de 1uF
    Resistencia=20000
    Capacitor=0.1e-6
    Fc=1/(2*math.pi*Resistencia*Capacitor) #Hz

    return dutycycle,Fc 
  

if __name__=='__main__':
    from firebase import firebase 
    firebase = firebase.FirebaseApplication("https://invernadero-c2130-default-rtdb.firebaseio.com/",None)

    portencia = firebase.get('/valores/potenciaVentiladorActualizadaa','')
    print(valor_dutycycle(portencia["value"]))