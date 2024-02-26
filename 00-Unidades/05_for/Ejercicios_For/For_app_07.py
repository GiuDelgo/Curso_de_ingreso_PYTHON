import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Giuliana
apellido: Delgobbo
---
Ejercicio: for_07
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. Informar si el número es PRIMO o no.
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
        mensaje = ""
        
        numero_ingresado = prompt ("Ingreso", "Ingresar un número")
        numero_ingresado = int (numero_ingresado)

        for i in range (1,numero_ingresado+1):
            
            if numero_ingresado % i == 0:
                contador_divisores += 1
        
        if contador_divisores > 2:
            mensaje = "El número NO es primo"
        else:
            mensaje = "El número ES primo"

        alert ("Resultado", mensaje)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()