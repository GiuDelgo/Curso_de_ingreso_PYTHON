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

        cantidad_candidatos = prompt("Candidatos", "Ingresar la cantidad de candidatos")

        while  cantidad_candidatos == None or cantidad_candidatos.isalpha() or int(cantidad_candidatos) == 0:
            cantidad_candidatos = prompt("Candidatos", "Volver a ingresar la cantidad de candidatos")

        cantidad_candidatos = int(cantidad_candidatos)

        while contador < cantidad_candidatos: 
            #NOMBRE 
            nombre = prompt("Nombre", "Ingresar nombre del candidato")

            while nombre == None or not nombre.isalpha:
                nombre = prompt("Nombre", "Ingresar nombre del candidato")

            #EDAD
            edad = prompt("Edad", "Ingresar la edad del candidato")
            
            while int(edad) <25:
                edad = prompt("Edad", "Volver a ingreasar edad del candidato")
            
            edad = int(edad)

            #CANTIDAD DE VOTOS
            cantidad_votos = prompt("Votos", "Ingresar la cantidad de votos del candidato")

            while int(cantidad_votos) == 0:
                cantidad_votos = prompt("Cantidad Invalida", "Volver a ingresar la cantidad de votos")

            cantidad_votos = int(cantidad_votos)

            #MAXIMOS/MINIMOS
            if contador == 0 or cantidad_votos<min_votos:
                min_votos = cantidad_votos
                min_votos_nombre = nombre
                min_votos_edad = edad  

            if contador == 0 or cantidad_votos>max_votos:
                max_votos = cantidad_votos
                max_votos_nombre = nombre  

            suma_edades += edad
            suma_votos += cantidad_votos

            contador += 1
        
        promedio_edades = suma_edades/contador

        mensaje = f"- Candidato con más votos: {max_votos_nombre} con {max_votos} votos.\n- Candidato con menos votos: {min_votos_nombre} de {min_votos_edad} años, con {min_votos} votos.\n- Promedio de edades de candidatos: {promedio_edades} años.\n- Total de votos emitidos: {suma_votos} votos."

        alert("Resultados",mensaje)
        

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
