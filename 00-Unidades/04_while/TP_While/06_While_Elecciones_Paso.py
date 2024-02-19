import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Giuliana
apellido: Delgobbo
---
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por alert

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):

        contador = 0
        nombre = ""
        edad = 0
        cantidad_votos = 0

        min_votos = 0
        min_votos_edad = 0
        min_votos_nombre = ""
        max_votos = 0
        max_votos_nombre = ""

        suma_edades = 0
        promedio_edades = 0

        suma_votos = 0

        alert("Ingreso datos","Ingresar los datos de los candidatos.\nPara salir de la carga presionar CANCELAR en cualquier ventana")

        while True: 
            #NOMBRE
            nombre = prompt("Nombre", "Ingresar el nombre del candidato")

                #VALIDACION/CANCELACION
            if nombre == None:
                break    

            #EDAD
                #VALIDACION/CANCELACION
            edad = prompt("Edad", "Ingresar la edad del candidato")
            if edad == None:
                break

            edad = int(edad)

            while edad < 25:
                edad = prompt("Edad Invalida", "Volver a ingresar la edad del candidato")
                edad = int(edad)

            #CANTIDAD DE VOTOS
                #VALIDACION/CANCELACION
            cantidad_votos = prompt("Votos", "Ingresar la cantidad de votos del candidato")
            if cantidad_votos == None:
                break
            
            cantidad_votos = int(cantidad_votos)

            while cantidad_votos < 0:
                cantidad_votos = prompt("Cantidad Invalida", "Volver a ingresar la cantidad de votos")
                cantidad_votos = int(cantidad_votos)
                
                #MAXIMOS/MINIMOS
            if  contador == 0:
                min_votos = cantidad_votos
                min_votos_nombre = nombre

                max_votos = cantidad_votos
                max_votos_nombre = nombre

            if cantidad_votos > max_votos:
                max_votos = cantidad_votos
                max_votos_nombre = nombre

            if cantidad_votos < min_votos:
                min_votos = cantidad_votos
                min_votos_nombre = nombre
                min_votos_edad = edad

            suma_edades = edad + suma_edades
            suma_votos = cantidad_votos + suma_votos

            contador += 1

        promedio_edades = suma_edades/contador

        mensaje = f"- Candidato con más votos: {max_votos_nombre} con {max_votos} votos.\n- Candidato con menos votos: {min_votos_nombre} de {min_votos_edad} años, con {min_votos} votos.\n- Promedio de edades de candidatos: {promedio_edades} años.\n- Total de votos emitidos: {suma_votos} votos."

        alert("Resultados",mensaje)
        

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
