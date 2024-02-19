import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Giuliana
apellido: Delgobbo
---
TP: Iluminación
---
Enunciado:
Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        PRECIO_X_LAMPARA = 800
        descuento = 0
        precio_sin_desc = 0
        precio_con_desc = 0
        descuento_adicional = 0
        
        marca = self.combobox_marca.get()
        cantidad_lamparas = int(self.combobox_cantidad.get())

        match (cantidad_lamparas):
            case 5:
                match (marca):
                    case "ArgentinaLuz":
                        descuento = 40
                    case _:
                        descuento = 30
            case 4:
                match (marca):
                    case "FelipeLamparas"|"ArgentinaLuz":
                        descuento = 25
                    case _:
                        descuento = 20
            case 3:
                match (marca):
                    case "ArgentinaLuz":
                        descuento = 15
                    case "FelipeLamparas":
                        descuento = 10
                    case _:
                        descuento = 5
            case 1|2:
                descuento = 0
            case _:
                descuento = 50

        precio_sin_desc = (cantidad_lamparas*PRECIO_X_LAMPARA) 
        precio_con_desc= precio_sin_desc - (precio_sin_desc*(descuento/100))

        mensaje = f"El total a abonar es {precio_con_desc} con un descuento del {descuento}% aplicado."

        if precio_con_desc > 4000:
                descuento_adicional = 5
                precio_con_desc = precio_con_desc - (precio_con_desc*(descuento_adicional/100))
                mensaje = f"El total a abonar es {precio_con_desc} con un descuento del {descuento}% aplicado.\n ***DESCUENTO ADICIONAL DEL {descuento_adicional}% APLICADO***"


        alert ("Precio",mensaje)
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()