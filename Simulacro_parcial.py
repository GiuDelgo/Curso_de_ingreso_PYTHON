import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Giuliana
apellido: Delgobbo
---
Un famoso casino de mar del plata,  requiere una app para controlar el egreso de dinero durante una jornada. Para ello se ingresa por cada ganador:

Nombre

Importe ganado (mayor o igual $1000)

Género (“Femenino”, “Masculino”, “Otro”)

Juego (Ruleta, Poker, Tragamonedas)


-------------------------------------------------------------
Necesitamos saber:

Nombre y género de la persona que más ganó.

Promedio de dinero ganado en Ruleta.

Porcentaje de personas que jugaron en el Tragamonedas.

Cuál es el juego menos elegido por los ganadores.

El nombre del jugador que ganó más dinero jugando Poker

Texto de la respuesta
'''
continuar = 0
nombre =  ""
importe_ganado = 0
genero = 0
juego = ""
contador_total_personas = 0

bandera = True
max_importe_ganado = 0
nombre_max_importe_ganado = ""
genero_max_importe_ganado = ""

suma_dinero_ruleta = 0
contador_ruleta = 0
promedio_dinero_ruleta = 0

contador_tragamonedas = 0
porcentaje_personas_tragamonedas = 0

contador_poker = 0

juego_menos_elegido = ""

max_importe_ganado_poker = 0
nombre_max_importe_ganado_poker = ""


#CARGA DE DATOS
while True:

    continuar = prompt("Ingreso", "Desea ingresar ganadores?")
    if continuar == None:
        break

    #NOMBRE
    nombre = prompt("Nombre", "Ingrese nombre")

    #IMPORTE GANADO
    importe_ganado = prompt ("Importe", "Ingrese importe ganado")

    while int(importe_ganado) < 1000:
        importe_ganado = prompt ("Importe", "Reingrese importe ganado")

    importe_ganado = int(importe_ganado)

    #GENERO
    genero = prompt("Género", "Ingrese género")

    while genero != "Femenino" and genero != "Masculino" and genero != "Otro":
        genero = prompt ("Género", "Reingrese género")

    #JUEGO
    juego = prompt("Juego", "Ingrese juego")

    while juego != "Ruleta" and juego != "Poker" and juego != "Tragamonedas":
        juego = prompt ("Juego", "Reingrese juego")
    
    #Cuál es el juego menos elegido por los ganadores.
    match juego:
        #Promedio de dinero ganado en Ruleta.
        case "Ruleta":
            suma_dinero_ruleta += importe_ganado
            contador_ruleta +=1
        case "Poker":
            contador_poker += 1
            #El nombre del jugador que ganó más dinero jugando Poker
            if bandera or importe_ganado > max_importe_ganado_poker:
                max_importe_ganado_poker = importe_ganado
                nombre_max_importe_ganado_poker = nombre

                bandera = False
        case "Tragamonedas":
        #Porcentaje de personas que jugaron en el Tragamonedas.
            contador_tragamonedas += 1
    
    #Nombre y género de la persona que más ganó
    if bandera or importe_ganado > max_importe_ganado:
        max_importe_ganado = importe_ganado
        nombre_max_importe_ganado = nombre
        genero_max_importe_ganado = genero

        bandera = False
    
    contador_total_personas += 1

#--------------RESULTADOS----------------

#Nombre y género de la persona que más ganó.
mensaje= f"La persona que más ganó es: {nombre_max_importe_ganado}, de género: {genero_max_importe_ganado}, con un total de: {max_importe_ganado}$"
print(mensaje)
print("------------------------------")

#Promedio de dinero ganado en Ruleta.
if contador_ruleta == 0:
    mensaje = "No se ingresaron jugadores de ruleta"
else: 
    promedio_dinero_ruleta = suma_dinero_ruleta/contador_ruleta
    mensaje = f"El promerio de dinero ganado en ruleta es {promedio_dinero_ruleta}$"
print(mensaje)
print("------------------------------")

#Porcentaje de personas que jugaron en el Tragamonedas.
porcentaje_personas_tragamonedas = (contador_tragamonedas*100)/contador_total_personas

mensaje = f"El porcentaje de personas que jugó el tragamonedas es: {porcentaje_personas_tragamonedas}%"
print(mensaje)
print("------------------------------")

#Cuál es el juego menos elegido por los ganadores.
if contador_poker < contador_ruleta and contador_poker < contador_tragamonedas:
    juego_menos_elegido = "Poker"
elif contador_ruleta < contador_tragamonedas:
    juego_menos_elegido = "Ruleta"
else:
    juego_menos_elegido = "Tragamonedas"

mensaje = f"El juego menos elegido por los ganadores es: {juego_menos_elegido}"
print(mensaje)
print("------------------------------")

#El nombre del jugador que ganó más dinero jugando Poker
if contador_poker == 0:
    mensaje = "No se ingresaron jugadores de poker"
else: 
    mensaje = f"La persona que más ganó en Poker es: {nombre_max_importe_ganado_poker}, con {max_importe_ganado_poker}$"
print(mensaje)
print("------------------------------")

