import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Giuliana    
apellido: Delgobbo
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):

        numero = 0 
        suma_positivos = 0 
        suma_negativos = 0 
        contador_positivos = 0
        contador_negativos = 0
        contador_ceros = 0 
        diferencia_positivos_negativos = 0 
        mensaje = ""

        while True:

            numero = prompt("Numero", "Ingersar un numero")
            
            if numero == None:
                break

            numero = int (numero)

            if numero < 0:
                suma_negativos = suma_negativos + numero
                contador_negativos += 1
            elif numero > 0:
                suma_positivos = suma_positivos + numero
                contador_positivos += 1
            else: 
                contador_ceros += 1
    
        diferencia_positivos_negativos = contador_positivos - contador_negativos

        mensaje = f"- Suma acumulada de N° negativos: {suma_negativos}\n- Suma acumulada de N° positivos: {suma_positivos}\n- Cantidad N° positivos ingresados: {contador_positivos}\n- Cantidad N° negativos ingresados: {contador_negativos}\n- Cantidad de ceros: {contador_ceros}\n- Diferencia entre cantidad de N° positivos ingresados y N° negativos: {diferencia_positivos_negativos}"
            
        alert ("Resultados", mensaje)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
