import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Giuliana    
apellido: Delgobbo
---
De 20 contenedores que llegan al puerto de Rosario, se deben pedir y validar los siguientes datos

Marca (no validar)
Categoría (peligroso, comestible, indumentaria)
Peso (entre 100 y 800)
Tipo de material (aluminio, hierro , madera)
Costo en $ (mayor a 0)

Pedir datos por prompt y mostrar por print, se debe informar:

Informe A- Cuál fue la categoría menos ingresada (peligroso, comestible, indumentaria)
Informe B- El porcentaje de contenedores por Tipo de material ( aluminio, hierro , madera)
Informe C- La marca y tipo del contenedor menos pesado
Informe D- La marca del contenedor peligroso con mayor costo
Informe E- El promedio de peso de todos los contenedores


'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):

        marca = ""
        categoria = ""
        peso = 0
        tipo_material = ""
        costo = 0

        contador_peligroso = 0
        contador_comestible = 0
        contador_indumentaria = 0

        contador_aluminio = 0
        porcentaje_aluminio = 0
        contador_hierro = 0
        porcentaje_hierro = 0
        contador_madera = 0
        porcentaje_madera = 0

        bandera = True
        peso_minimo = 0
        marca_peso_minimo = ""
        tipo_material_peso_minimo = ""

        bandera_2 = True
        max_costo = 0
        marca_max_costo = ""

        acumulador_peso = 0
        promedio_peso = 0

        #CARGA DE DATOS
        for i in range (1,21):

            #MARCA
            marca = prompt ("Marca", "Ingresar la marca")

            #CATEGORÍA
            categoria = prompt("Categoría", "Ingresar categoría")

            while categoria == None or categoria != "peligroso" and categoria != "comestible" and categoria != "indumentaria":
                categoria = prompt("Categoría", "Reingresar categoría")
            
            #PESO
            peso = prompt ("Peso", "Ingresar peso")

            while peso == None or int(peso) < 100 or int(peso) > 800:
                peso = prompt ("Peso", "Reingresar peso")
            
            peso = int(peso)

            #TIPO DE MATERIAL
                
            tipo_material = prompt ("Material", "Ingresar tipo de material")

            while tipo_material == None or tipo_material != "aluminio" and tipo_material !="hierro" and tipo_material !="madera":
                tipo_material = prompt ("Material", "Reingresar tipo de material")

            #COSTO
            costo = prompt ("Costo", "Ingresar costo")

            while costo == None or int (costo) <= 0:
                costo = prompt ("Costo", "Reingresar costo")

            costo = int(costo)

            #Informe A | Informe D
            match categoria:
                case "peligroso":
                    contador_peligroso += 1

                    if bandera_2 or max_costo < costo:
                        max_costo = costo
                        marca_max_costo = marca
                        bandera_2 = False
                case "comestible":
                    contador_comestible += 1
                case "indumentaria":
                    contador_indumentaria += 1

            #Informe B
            match tipo_material:
                case "aluminio":
                    contador_aluminio += 1
                case "hierro":
                    contador_hierro += 1
                case "madera":
                    contador_madera += 1

            #Informe C
            
            if bandera or peso_minimo > peso:
                peso_minimo = peso
                marca_peso_minimo = marca
                tipo_material_peso_minimo = tipo_material
                bandera = False

            #Informe E
            acumulador_peso += peso

            #NRO CONTENEDOR
            alert ("Estado",f"Contenedor N° {i} cargado")

        #****************RESULTADOS**************#
            
        #Informe A- Cuál fue la categoría menos ingresada (peligroso, comestible, indumentaria)
        
        if contador_peligroso < contador_comestible and contador_peligroso < contador_indumentaria:
            mensaje = "La categoría menos ingresada fue: Peligroso\n"
        elif contador_comestible < contador_indumentaria: 
            mensaje = "La categoría menos ingresada fue: Comestible\n"
        else: 
            mensaje = "La categoría menos ingresada fue: Indumentaria\n"

        #Informe B- El porcentaje de contenedores por Tipo de material ( aluminio, hierro , madera)
        porcentaje_aluminio = (contador_aluminio * 100)/20
        porcentaje_hierro = (contador_hierro * 100)/20
        porcentaje_madera = (contador_madera * 100)/20
        
        mensaje += f"Porcentaje de contenedores Aluminio: {porcentaje_aluminio}%\nPorcentaje de contenedores Hierro: {porcentaje_hierro}%\nPorcentaje de contenedores Madera: {porcentaje_madera}%\n"

        #Informe C- La marca y tipo del contenedor menos pesado
        mensaje += f"El contenedor con menos peso es de la marca: {marca_peso_minimo}. Transporta {peso_minimo} toneladas de {tipo_material_peso_minimo}.\n"
        
        #Informe D- La marca del contenedor peligroso con mayor costo
        mensaje += f"La marca del contenedor peligroso con mayor costo es {marca_max_costo} con un total de ${max_costo}.\n"

        #Informe E- El promedio de peso de todos los contenedores
        promedio_peso = acumulador_peso/20

        mensaje += f"El promedio de peso de todos los contenedores es: {promedio_peso}"

        #MENSAJE
        print(mensaje)



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
