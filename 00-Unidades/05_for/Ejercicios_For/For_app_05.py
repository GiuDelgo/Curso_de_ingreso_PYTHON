import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Giuliana
apellido: Delgobbo
---
Ejercicio: for_05
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. mostrar los números pares desde 
el 1 al número ingresado, y mostrar la cantidad de números pares encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero_ingresado = 0
        numero_par = 0
        contador_pares = 0
        lista_pares = ""

        numero_ingresado = prompt ("Ingreso", "Ingresar un numero")
        numero_ingresado = int(numero_ingresado)

        for i in range (1,numero_ingresado+1):

            if i % 2 == 0:
                numero_par = str(i) + " "

                contador_pares += 1

                lista_pares += numero_par

        mensaje = f"Lista de N° pares: {lista_pares}\nCantidad de N° pares: {contador_pares}"

        alert ("Resultados", mensaje)
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()