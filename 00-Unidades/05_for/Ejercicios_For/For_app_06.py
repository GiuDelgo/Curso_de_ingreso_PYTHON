import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Giuliana
apellido: Delgobbo
---
Ejercicio: for_06
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. mostrar los números divisores desde el 1 al número ingresado, 
y mostrar la cantidad de números divisores encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        
        numero_ingresado = 0
        divisor_num_ingresado = 0
        lista_divisores = ""
        contador_divisores = 0

        numero_ingresado = prompt("Ingreso", "Ingresar un número")
        numero_ingresado = int(numero_ingresado)

        for i in range (1,numero_ingresado+1):

            if numero_ingresado % i == 0:

                divisor_num_ingresado = str (i)
                
                lista_divisores += divisor_num_ingresado + " "

                contador_divisores += 1

        mensaje = f"Lista de divisores: {lista_divisores}\nCantidad de divisores encontrados: {contador_divisores}"

        alert("Resultados", mensaje)

            
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()