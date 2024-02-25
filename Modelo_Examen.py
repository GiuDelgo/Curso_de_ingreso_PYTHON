import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter



'''
UTN Tecnologies, una reconocida software factory se encuentra en la busqueda de ideas para su proximo desarrollo en python, 
que promete revolucionar el mercado. 
Las posibles aplicaciones son las siguientes: 
# Inteligencia artificial (IA),
# Realidad virtual/aumentada (RV/RA), 
# Internet de las cosas (IOT)


Para ello, realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas:

Los datos a ingresar por cada encuestado son:
    * nombre del empleado
    * edad (no menor a 18)
    * genero (Masculino - Femenino - Otro)
    * tecnologia (IA, RV/RA, IOT)   

En esta opción, se ingresaran empleados hasta que el usuario lo desee.

Una vez finalizado el ingreso, mostrar:

    #!X 1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive.
    #!X 2) - Tecnología que mas se votó.
    #!X 3) - Porcentaje de empleados por cada genero
    #!X 4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre 18 y 25 o entre 33 y 42.  
    #!X 5) - Promedio de edad de los empleados de genero Femenino que votaron por IA
    #!X 6) - Nombre y género del empleado que voto por RV/RA con menor edad.

'''
#no sabemos la cantidad de iteraciones asi que programamos un while true

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):
    #ANTES DEL WHILE
        seguir = True #bandera

        contador_masculino_IOT_IA = 0

        contador_IA = 0
        contador_IOT = 0
        contador_RV_RA = 0

        contador_femenino = 0
        contador_masculino = 0
        contador_otro = 0

        contador_OIT_rango  = 0
        porcentaje_IOT_rango = 0

        contador_femenino_IA = 0
        acumulador_edad_femenino_IA = 0
        promedio_edad_femenino_IA = 0

        edad_minima = 0
        nombre_minimo = 0 

    #DURANTE EL WHILE
        while seguir:

            nombre = input("Ingrese nombre: ")

            edad = input("Ingrese la edad: ")
            edad = int(edad)
            while edad < 18:
                edad = input("Reingrese la edad: ")
                edad = int(edad)

            genero = input("Ingrese género: ")
            while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
                genero = input("Reingrese género: ")

            tecnologia = input("Ingrese tecnología: ")
            while tecnologia != "IA" and tecnologia != "RV/RA" and tecnologia != "IOT":
                tecnologia = input("Reingrese tecnología: ")

            #!X 2) - Tecnología que mas se votó.
            # if tecnologia == "IA":
            #     contador_IA += 1
            # elif tecnologia == "IOT":
            #     contador_IOT += 1
            # else:
            #     contador_RV_RA += 1
            ############################################
            match (tecnologia):
                case "IA":
                    contador_IA += 1
                case "RV/RA":
                    contador_RV_RA += 1
                    #!X 6) - Nombre y género del empleado que voto por RV/RA con menor edad.
                    if contador_RV_RA == 1 or edad < edad_minima:
                        edad_minima = edad
                        nombre_minimo = nombre
                        genero_minimo = genero
                case "IOT":
                    contador_IOT +=1
                    #!X 4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre 18 y 25 o entre 33 y 42.  
                    if edad >= 18 and edad <=25 or edad >= 33 and edad <= 42:
                        contador_OIT_rango += 1
                
            #!X 3) - Porcentaje de empleados por cada genero
            match genero:
                case "Femenino":
                    contador_femenino += 1
                    if tecnologia == "IA":
                        contador_femenino_IA +=1
                        acumulador_edad_femenino_IA += edad
                case "Masculino":
                    contador_masculino += 1
                    #!X 1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive.
                    if (tecnologia == "IOT" or tecnologia == "IA") and edad >= 25 and edad <= 50:
                        contador_masculino_IOT_IA += 1
                case "Otro":
                    contador_otro +=1

            seguir = question("Seguir", "Desea continuar?")

    #DESPUES DEL WHILE
        #!X 2) - Tecnología que mas se votó.
        if contador_IOT > contador_IA and contador_IOT > contador_RV_RA:
            tecnologia_mas_votada = "IOT"
        elif contador_IA > contador_RV_RA:
            tecnologia_mas_votada = "IA"
        else: 
            tecnologia_mas_votada = "RV/RA"

        #!X 3) - Porcentaje de empleados por cada genero
        total_empleados = contador_otro + contador_femenino + contador_masculino
        porcentaje_femenino = (contador_femenino * 100) / total_empleados
        porcentaje_masculino = (contador_masculino * 100) / total_empleados
        #  
        porcentaje_otro = 100 - (porcentaje_femenino + porcentaje_masculino) #El procesador no sabe restar, entonces conviene sacarle una resta y agregarle una suma para que sea más performante

        #!X 4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre 18 y 25 o entre 33 y 42.  
        porcentaje_IOT_rango = (contador_OIT_rango*100)/total_empleados

        #!X 5) - Promedio de edad de los empleados de genero Femenino que votaron por IA
        if contador_femenino_IA > 0:
            promedio_edad_femenino_IA = acumulador_edad_femenino_IA/contador_femenino_IA
        else:
            promedio_edad_femenino_IA = "No se pudo calcular el promedio. No se ingresaron femeninos que votaron IA."

        print(f"1. Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive: {contador_masculino_IOT_IA}")
        print(f"2. La más votada fue: {tecnologia_mas_votada}")
        print(f"3. Porcentajes:\n\tFemenino: {porcentaje_femenino}%\n\tMasculino: {porcentaje_masculino}%\n\tOtro: {porcentaje_otro}%")
        print(f"4. Porcentaje que voto IOT rango: {porcentaje_IOT_rango}")
        print(f"5. Promedio: {promedio_edad_femenino_IA}")

        if contador_RV_RA == 0:
            print(f"6. No se ingreso el minimo")
        else:
            print(f"6.  {edad_minima} -- {nombre_minimo} -- {genero_minimo}")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
