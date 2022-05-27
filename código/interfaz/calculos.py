import math
from firebase import firebase 

firebase = firebase.FirebaseApplication("https://invernadero-c2130-default-rtdb.firebaseio.com/",None)

tempAnt = 0
errorp = 0
serror = 0


#constantes controlador PID
kp = 0.02
ki = 0.005
kd = 0.01
temp = 22

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
 

#Vp=155.58 V
#VRMS=Vp*0.707=110V
#P=60W
#Rfoco=240
#V=sqrt(R*P)

#Irms=V/R=120*240=0.5A
#Im=sqrt(2)*Irms=0.7A


def focoIncandesente(potencia):
    #Se calculo con la potencia del foco con la ecuacion de angulo de disparo en el TRIAC
    #Pf=sqrt((1/pi)*(pi-alfa+(Sin(2*alfa)/2)))
    #alfa=algulo de disparo
    potencia=int(potencia)

    powerFactor={
        #PorcetanjeDisparo:alfa()
        0   :0,
        1   :0.01,
        2:  0.1,
        3:  0.15,
        4:  0.2,
        5:  0.3,
        6:  0.35,
        7:  0.4,
        8:  0.45,
        9:  0.5,
        10: 0.55,
        11: 0.65,
        12: 0.7,
        13: 0.75,
        14: 0.8,
        15: 85,
        16: 0.9,
        17: 0.95,
        18: 1,
        19: 1.05,
        20: 1.1,
        21: 1.2,
        22: 1.25,
        23: 1.3,
        24: 1.35,
        25: 1.38,
        26: 1.4,
        27: 1.45,
        28: 1.5,
        29: 1.55,
        30: 1.6,
        31: 1.65,
        32: 1.7,
        33: 1.75,
        34: 1.8,
        35: 1.83,
        36: 1.85,
        37: 1.9,
        38: 1.95,
        39: 2,
        40: 2.03,
        41: 2.05,
        42: 2.1,
        43: 2.15,
        44: 2.18,
        45: 2.2,
        46: 2.25,
        47: 2.28,
        48: 2.3,
        49: 2.35,
        50: 2.4,
        51: 2.42,
        52: 2.45,
        53: 2.48,
        54: 2.5,
        55: 2.53,
        56: 2.55,
        57: 2.6,
        58: 2.63,
        59: 2.65,
        60: 2.68,
        61: 2.7,
        62: 2.73,
        63: 2.75,
        64: 2.78,
        65: 2.8,
        66: 2.81,
        67: 2.83,
        68: 2.85,
        69: 2.88,
        70: 2.9,
        71: 2.91,
        72: 2.93,
        73: 2.95,
        74: 2.98,
        75: 2.99,
        76: 3,
        77: 3.02,
        78: 3.03,
        79: 3.05,
        80: 3.06,
        81: 3.07,
        82: 3.09,
        83: 3.1,
        84: 3.11,
        85: 3.12,
        86: 3.13,
        87: 3.14,
        98: 3.15,
        89: 3.155,
        90: 3.16,
        91: 3.17,
        92: 3.17,
        93: 3.18,
        94: 3.18,
        95: 3.18,
        96: 3.19,
        97: 3.19,
        98: 3.19,
        99: 3.19,
        100:    3.199999
    }

    #Usamos a 60Hz
    f=60
    tiempoDisparo=(powerFactor[potencia]/(2*math.pi*f))*1000
    

    return powerFactor[potencia],tiempoDisparo

#Control de temperatura 
def tempPID(temp):
    tempAnt = temp
    tempAux = (firebase.get('/valores/temperaturaInicial',''))
    temp = int(tempAux["value"])
    while tempAnt != temp:
        tempAnt = controlPID(temp,tempAnt)

    return tempAnt


#controlador PID
def  controlPID(tempP, tempAnt):
    global errorp,serror,temp
    error_control = tempP - tempAnt 
    tempAnt = (errorp * kd ) + (error_control * kp ) + (serror * ki )
    temp = max(min(150,temp),-55)
    errorp = error_control
    serror = serror + error_control
    print ("teperatura",tempAnt)
    return int(tempAnt)
      
