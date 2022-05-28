# !/usr/bin/python3
from tkinter import *
from calculos import *
from firebase import firebase

root = Tk()
root.title('Control invernadero')
root.geometry("1080x720")




firebase = firebase.FirebaseApplication("https://invernadero-c2130-default-rtdb.firebaseio.com/",None)
background = PhotoImage(file="invernadero.png")
imagen_label = Label(root, image=background)
imagen_label.place(x=0,y=0, relwidth=1, relheight=1)

var = StringVar()
label = Label( root, text="Control invernadero", anchor = CENTER, font=('Times 36'), fg="white" ,bg="#41aa5e")
label.config(width=200)

temp = firebase.get('/valores/temperaturaInicial','')
temp = temp["value"]

#textVariable
#var.set("Control invernadero")


#Labels de temperatura
temperatura_label = Label( root, text="Temperatura:", font=('Sans 12'), bg="white")
temperatura_label.place(x=50, y=100)
temperatura_label = Label( root, text="Rango: 15C - 30C", font=('Sans 8'), bg="white")
temperatura_label.place(x=50, y=150)  


#Labels de potencia
radiador_label = Label( root, text="Potencia del radiador:", font=('Sans 12'), bg="white")
radiador_label.place(x=50, y=250)
radiador_label = Label( root, text="Rango 0 %  a 100%", font=('Sans 8'), bg="white")
radiador_label.place(x=50, y=300)
factorF_label = Label( root, text="Factor de potencia ", font=('Sans 8'), bg="white")
factorF_label.place(x=50, y=325)
tiempo_label = Label( root, text="Tiempo de disparo (ms) ", font=('Sans 8'), bg="white")
tiempo_label.place(x=50, y=370)


#Hora irrigacion inicial
irrigacion_inicial_label = Label( root, text="Hora inicial irrigacion:", font=('Sans 12'), bg="white")
irrigacion_inicial_label.place(x=50, y=425)




#Hora temperatura inicial
temp_inicial_label = Label( root, text="Hora inicial temperatura:", font=('Sans 12'), bg="white")
temp_inicial_label.place(x=50, y=525)



#Estado
estado_label = Label( root, text="Estado", font=('Sans 12'), bg="white")
estado_label.place(x=50, y=600)



#Ventilador
ventilador_label = Label( root, text="Potencia del ventilador:", font=('Sans 12'), bg="white")
ventilador_label.place(x=600, y=250)
ventilador_label = Label( root, text="Rango 0mW - 600mW", font=('Sans 8'), bg="white")
ventilador_label.place(x=600, y=300)
factorF_label = Label( root, text="Porcentaje de potencia  ", font=('Sans 8'), bg="white")
factorF_label.place(x=600, y=325)

tiempo_label = Label( root, text="Frecuencia del ventilador ", font=('Sans 8'), bg="white")
tiempo_label.place(x=600, y=370)


#Hora irrigacion final
irrigacion_final_label = Label( root, text="Hora final irrigacion:", font=('Sans 12'), bg="white")
irrigacion_final_label.place(x=600, y=425)


#Hora temperatura final
temp_final_label = Label( root, text="Hora final temperatura:", font=('Sans 12'), bg="white")
temp_final_label.place(x=600, y=525)

#imagenes iniciales 

termometro = PhotoImage(file = "imagenes/10grados.png")
termometro = termometro.subsample(2)
termometro_img = Label(root, image = termometro)
#termometro_img =termometro.subsample(2)
#foco_img.configure(bg = background)
termometro_img.place(x=300, y=60)


foco = PhotoImage(file = "imagenes/foco0.png")
foco = foco.subsample(2)
foco_img = Label(root, image = foco)
#foco_img.configure(bg = background)
foco_img.place(x=300, y=280)

vent = PhotoImage(file = "imagenes/ventilador.png")
vent = vent.subsample(4)
vent_img = Label(root, image = vent)
#foco_img.configure(bg = background)
vent_img.place(x=850, y=280)


while(1):
    estadoSistema=firebase.get('/valores/StatusIrrigacion','')
    if(estadoSistema["value"]=='2'):
    	    #Valores de firebase
	    HoraIF = StringVar()
	    HoraIF_2 = firebase.get('/valores/HoraIndicadaFinal','')
	    HoraIF.set(HoraIF_2["value"])

	    HoraII = StringVar()
	    HoraII_2 = firebase.get('/valores/HoraIndicadaInicial','')
	    HoraII.set(HoraII_2["value"])
	    #########################################################################################
	    IrrII = StringVar()
	    IrrII_2 = firebase.get('/valores/HoraIndicadaIrrigacionInicial','')
	    IrrII.set(IrrII_2["value"])

	    IrrIF = StringVar()
	    IrrIF_2 = firebase.get('/valores/HoraIndicadaIrrigacionFinal','')
	    IrrIF.set(IrrIF_2["value"])

	    StatIrr = StringVar()
	    StatIrr_2 = firebase.get('/valores/statusIrrigacionStr','')
	    StatIrr.set(StatIrr_2["value"])

	    PotRad = StringVar()
	    powerFactor= StringVar()
	    tiempoDisparo= StringVar()
	    PotRad_2,powerFactor_2,tiempoDisparo_2 = '0','0','0'
	    PotRad.set(PotRad_2)
	    powerFactor.set(powerFactor_2)
	    tiempoDisparo.set(tiempoDisparo_2)



	    PotVent = StringVar()
	    dutycycle = StringVar()
	    Fc = StringVar()
	    PotVent_2,dutycycle_2,Fc_2 ='0','0','0'
	    PotVent.set(PotVent_2)
	    dutycycle.set(dutycycle_2)
	    Fc.set(Fc_2)

	    StatIrrStr = StringVar()
	    StatIrrStr.set(StatIrr_2["value"])

	    TempInicial = StringVar()
	    temp = '0'
	    TempInicial.set(temp)
	    temp = int(temp)

	    termometro = PhotoImage(file = "imagenes/10grados.png")
	    termometro = termometro.subsample(2)
	    termometro_img = Label(root, image = termometro)
	    termometro_img.place(x=300, y=60)

	    foco = PhotoImage(file = "imagenes/foco0.png")
	    foco = foco.subsample(2)
	    foco_img = Label(root, image = foco)
	    foco_img.place(x=300, y=280)

    else:
	    #Valores de firebase
	    HoraIF = StringVar()
	    HoraIF_2 = firebase.get('/valores/HoraIndicadaFinal','')
	    HoraIF.set(HoraIF_2["value"])

	    HoraII = StringVar()
	    HoraII_2 = firebase.get('/valores/HoraIndicadaInicial','')
	    HoraII.set(HoraII_2["value"])
	    #########################################################################################
	    IrrII = StringVar()
	    IrrII_2 = firebase.get('/valores/HoraIndicadaIrrigacionInicial','')
	    IrrII.set(IrrII_2["value"])

	    IrrIF = StringVar()
	    IrrIF_2 = firebase.get('/valores/HoraIndicadaIrrigacionFinal','')
	    IrrIF.set(IrrIF_2["value"])

	    StatIrr = StringVar()
	    StatIrr_2 = firebase.get('/valores/StatusIrrigacion','')
	    StatIrr.set(StatIrr_2["value"])

	    PotRad = StringVar()
	    powerFactor= StringVar()
	    tiempoDisparo= StringVar()
	    PotRad_2 = firebase.get('/valores/potenciaRadiadorNueva','')
	    powerFactor_2,tiempoDisparo_2 = focoIncandesente (PotRad_2["value"])
	    PotRad.set(PotRad_2["value"])
	    powerFactor.set(powerFactor_2)
	    tiempoDisparo.set(tiempoDisparo_2)
	    Pot = int(PotRad_2["value"])

	    if (Pot == 0):
	    	foco = PhotoImage(file = "imagenes/foco0.png")
	    	foco = foco.subsample(2)
	    	foco_img = Label(root, image = foco)
	    	foco_img.place(x=300, y=280)
	    else:
	    	if (Pot > 0) and (Pot <= 50):
	    		foco = PhotoImage(file = "imagenes/foco50.png")
	    		foco = foco.subsample(2)
	    		foco_img = Label(root, image = foco)
	    		foco_img.place(x=300, y=280)
	    	else:
	    		if  (Pot > 50) and (Pot <= 100):    		
	    			foco = PhotoImage(file = "imagenes/foco100.png")
	    			foco = foco.subsample(2)
	    			foco_img = Label(root, image = foco)
	    			foco_img.place(x=300, y=280)



	    PotVent = StringVar()
	    dutycycle = StringVar()
	    Fc = StringVar()
	    PotVent_2 = firebase.get('/valores/potenciaVentiladorActualizadaa','')
	    dutycycle_2,Fc_2 = valor_dutycycle(PotVent_2["value"])
	    PotVent.set(PotVent_2["value"])
	    dutycycle.set(dutycycle_2)
	    Fc.set(Fc_2)

	    StatIrrStr = StringVar()
	    StatIrrStr_2 = firebase.get('/valores/statusIrrigacionStr','')
	    StatIrrStr.set(StatIrrStr_2["value"])

	    TempInicial = StringVar()
	    temp = tempPID(temp) 
	    TempInicial.set(temp)
	    temp = int(temp)
	    temp_A = (firebase.get('/valores/temperaturaInicial',''))
	    temp2 = int(temp_A["value"]) 

	    if (temp2 >= 10) and (temp2 < 20):
	    	termometro = PhotoImage(file = "imagenes/10grados.png")
	    	termometro = termometro.subsample(2)
	    	termometro_img = Label(root, image = termometro)
	    	termometro_img.place(x=300, y=60)
	    else:
	    	if (temp2 >= 20) and (temp2 < 30):
	    		termometro = PhotoImage(file = "imagenes/20grados.png")
	    		termometro = termometro.subsample(2)
	    		termometro_img = Label(root, image = termometro)
	    		termometro_img.place(x=300, y=60)
	    	else:
	    		if  (temp2 == 30):    		
	    			termometro = PhotoImage(file = "imagenes/30grados.png")
	    			termometro = termometro.subsample(2)
	    			termometro_img = Label(root, image = termometro)
	    			termometro_img.place(x=300, y=60)



    	


    temp_num = Entry(root, textvariable=TempInicial, font=('Sans 12'), bg="white")
    temp_num.place(x=50, y=125)
    
    temp_inicial_num = Entry(root, textvariable=PotRad, font=('Sans 12'), bg="white")
    temp_inicial_num.place(x=50, y=275)
    
    powerFactor_num = Entry(root, textvariable=powerFactor , font=('Sans 12'), bg="white")
    powerFactor_num.place(x=50, y=345)
    
    tiempoDisparo_num = Entry(root, textvariable=(tiempoDisparo), font=('Sans 12'), bg="white")
    tiempoDisparo_num.place(x=50, y=390)
    
    irr_inicial_num = Entry(root, textvariable=IrrII, font=('Sans 12'), bg="white")
    irr_inicial_num.place(x=50, y=450)
    
    temp_inicial_num = Entry(root, textvariable=HoraII, font=('Sans 12'), bg="white")
    temp_inicial_num.place(x=50, y=550)
    status_str = Entry(root, textvariable=StatIrrStr, font=('Sans 12'), bg="white")
    status_str.place(x=50, y=625)
    powerFactor_num = Entry(root, textvariable=dutycycle , font=('Sans 12'), bg="white")
    powerFactor_num.place(x=600, y=345)
    temp_inicial_num = Entry(root, textvariable=PotVent, font=('Sans 12'), bg="white")
    temp_inicial_num.place(x=600, y=275)
    tiempoDisparo_num = Entry(root, textvariable=Fc, font=('Sans 12'), bg="white")
    tiempoDisparo_num.place(x=600, y=390)
    
    irr_final_num = Entry(root, textvariable=IrrIF, font=('Sans 12'), bg="white")
    irr_final_num.place(x=600, y=450)
    temp_final_num = Entry(root, textvariable=HoraIF, font=('Sans 12'), bg="white")
    temp_final_num.place(x=600, y=550)


    

    label.pack()
    root.update()
root.mainloop()
