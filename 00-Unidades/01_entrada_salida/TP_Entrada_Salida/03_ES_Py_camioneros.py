import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
TP: ES_Camioneros
---
Enunciado:

3.	Para el departamento de logística:

	A.	Es necesario saber la cantidad camiones que harian falta para transportar los materiales que se utilizarán para la construcción de un edificio. 
    Para ello, se ingresa la cantidad de toneladas necesarias de materiales a transportar. El programa deberá informar la cantidad de camiones, 
    sabiendo que cada uno de ellos puede transportar por viaje 3500kg

    B.	A partir del ingreso de la cantidad de kilómetros que tiene que recorrer estos camiones para llegar al destino de la obra, 
    necesitamos que el programa informe cual es el tiempo (en horas) que tardará cada uno de los camiones, 
    si sabemos que cada camión puede ir a una velocidad máxima y constante de 90 km/h  

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Toneladas")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_toneladas = customtkinter.CTkEntry(master=self)
        self.txt_toneladas.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Kilómetros")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_kilometros = customtkinter.CTkEntry(master=self)
        self.txt_kilometros.grid(row=1, column=1)
       
        self.btn_cantidad_camiones = customtkinter.CTkButton(master=self, text="Calcular cantidad de camiones", command=self.btn_cantidad_camiones_on_click)
        self.btn_cantidad_camiones.grid(row=3, pady=10, padx=30 ,columnspan=2, sticky="nsew")
        
        self.btn_tiempo_llegada = customtkinter.CTkButton(master=self, text="Calcular tiempo de llegada", command=self.btn_tiempo_llegada_on_click)
        self.btn_tiempo_llegada.grid(row=4, pady=10, padx=30, columnspan=2, sticky="nsew")
    
    def btn_cantidad_camiones_on_click(self):
        
        toneladas = float (self.txt_toneladas.get())

        kilos = toneladas * 1000 #De tonelada a kg

        #cant_camiones = (kilos + 3500 - 1) / 3500 #Calculo cant de camiones necesarios. Solo funciona para valores enteros. En otro tipo de problema deberia usar if. 
                                             #Pero vamos a suponer valores enteros en kg, dado que 0,1 kg = 100g despreciables para valores en toneladas. 
        
        #cant_camiones = int(cant_camiones) #Paso el valor de cantidad de camiones a nro enteros. X ej si ingreso 7 toneladas (700kg) el resultado de la ecuacion anterior es 2.99. 
                                 #Pasando la rta a entero es que funciona la ecuacion anterior, ya que el programa redondea para abajo, dando como resultado 2.
                                 #Si el valor ingresado es 7.1 (7100 kg) el resultado de la ecuacion es 3, y asi...
        
        cant_camiones = kilos/3500

        import math

        cant_camiones = math.ceil(cant_camiones)
        
        mensaje = f"La cantidad de camiones necesarios es {cant_camiones}"

        alert("Camiones",mensaje)

        self.txt_toneladas.delete(0,"end")

    def btn_tiempo_llegada_on_click(self):

        distancia_km = float (self.txt_kilometros.get())

        tiempo = distancia_km/90 

        #Ahora paso el rasultado a sist. sexagesimal, separarando horas y minutos
                
        minutos =  (tiempo - int (tiempo))*60 #Aislo los decimales del resultado anterior y los multiploco x 60 para obtener los minutos

        minutos = int(minutos)

        horas = int(tiempo)

        mensaje = f"El tiempo restante de viaje es {horas} horas y {minutos} minutos"

        alert ("Tiempo", mensaje)

        self.txt_kilometros.delete(0,"end")
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()