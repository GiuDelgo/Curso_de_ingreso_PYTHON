import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Giuliana
apellido: Delgobbo
---
Ejercicio: for_08
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. 
Mostrar cada número primo entre 1 y el número ingresado, e informar la cantidad de números primos encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero_ingresado = 0
        contador_divisores = 0
        numero_primo = 0
        lista_primos = ""
        contador_primos = 0

        numero_ingresado = prompt("Ingreso","Ingresar un número")
        numero_ingresado = int(numero_ingresado)

        for i in range (1,numero_ingresado+1):
            
            contador_divisores = 0

            for r in range (1,i+1):
                if i % r == 0:
                    contador_divisores +=1
            
            if contador_divisores <= 2:
                numero_primo = str(i) + " "

                lista_primos += numero_primo

                contador_primos += 1
        
        mensaje = f"Los numeros primos son: {lista_primos}\nLa cantidad de numero primos es: {contador_primos}"

        alert("Resultados", mensaje)





if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()