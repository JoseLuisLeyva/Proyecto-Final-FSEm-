# !/usr/bin/python3
from tkinter import *

root = Tk()
root.title('Control invernadero')
root.geometry("1080x720")

background = PhotoImage(file="invernadero.png")
imagen_label = Label(root, image=background)
imagen_label.place(x=0,y=0, relwidth=1, relheight=1)

var = StringVar()
label = Label( root, text="Control invernadero", anchor = CENTER, font=('Times 36'), fg="white" ,bg="#41aa5e")
label.config(width=200)
#textVariable
#var.set("Control invernadero")

#Labels de temperatura
temperatura_label = Label( root, text="Temperatura:", font=('Sans 12'), bg="white")
temperatura_label.place(x=50, y=100)

temperatura_label = Label( root, text="Rango: 10C - 30C", font=('Sans 8'), bg="white")
temperatura_label.place(x=50, y=175)  


#Labels de potencia
radiador_label = Label( root, text="Potencia del radiador:", font=('Sans 12'), bg="white")
radiador_label.place(x=50, y=250)

radiador_label = Label( root, text="Rango 1000W - 2000W", font=('Sans 8'), bg="white")
radiador_label.place(x=50, y=325)

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

ventilador_label = Label( root, text="Rango 1000W - 2000W", font=('Sans 8'), bg="white")
ventilador_label.place(x=600, y=325)

#Hora irrigacion final
irrigacion_final_label = Label( root, text="Hora final irrigacion:", font=('Sans 12'), bg="white")
irrigacion_final_label.place(x=600, y=425)

#Hora temperatura final
temp_final_label = Label( root, text="Hora final temperatura:", font=('Sans 12'), bg="white")
temp_final_label.place(x=600, y=525)

label.pack()
root.mainloop()
