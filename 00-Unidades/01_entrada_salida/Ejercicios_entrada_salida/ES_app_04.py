import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Giuliana
apellido: Delgobbo
tutor: Alejandro
---
Ejercicio: entrada_salida_04
---
Enunciado:
Al presionar el botón  'Mostrar', se deberá obtener un nombre utilizando el Dialog Prompt 
y luego mostrarlo en la caja de texto txt_nombre (.delete / .insert )
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Nombre")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_nombre = customtkinter.CTkEntry(master=self)
        self.txt_nombre.grid(row=0, column=1)
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        nombre=prompt("Nombre","Ingrese su nombre")
        #self.txt_nombre.delete(0,30) #se marca el inicio y el fin de la cantidad de caracteres a borrar 
        #self.txt_nombre.delete(0,tkinter.END)
        #self.txt_nombre.delete(0,len(self.txt_nombre.get())) el programa va del cero a la cantidad de caracteres que el usuario haya ingresadp

        self.txt_nombre.delete(0,"end") #opcion nativa de python

        self.txt_nombre.insert(0, nombre) #el cero marca la posicion desde donde se escribe el txt en el txt box
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()