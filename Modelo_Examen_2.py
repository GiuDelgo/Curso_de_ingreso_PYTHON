'''
Se nos ha solicitado desarrollar una aplicación para llevar registro de las entradas vendidas en el Estadio River 
Plate, para el concierto de Taylor Swift. Para ello, se solicitará al usuario la siguiente información al momento de 
comprar cada entrada:

Al presionar el voton se debera pedir la carga de los siguientes datos, hasta que el usuario lo desee:

Los datos que deberas pedir para los ventas son:
    * Nombre del comprador
    * Edad (no menor a 16)
    * Género (Masculino, Femenino, Otro)
    * Tipo de entrada (General, Campo delantero, Platea)
    * Medio de pago (Crédito, Efectivo, Débito) 
    * Precio de la entrada (Se debe calcular)

Para cada venta, se calculará el total a pagar en función del tipo de entrada elegida, 
el medio de pago y su precio correspondiente.

 * Lista de precios: 
        * General: $16000
        * Campo:   $25000
        * Platea:  $30000

Las entradas adquiridas con tarjeta de crédito tendrán un 20% de descuento sobre el 
precio de la entrada, mientras que las adquiridas con tarjeta de débito un 15%. 

Al finalizar la carga, el programa debera mostrar los siguientes informes:

    #! 1) - Determina el género más frecuente entre las personas que compraron entradas de tipo "Campo".
    #! 2) - Determina cuántas personas compraron entradas de tipo "General" pagando con tarjeta 
    #!          de crédito y su edad promedio.
    #! 3) - Calcula el porcentaje de personas que compraron entradas de tipo "Platea" y 
    #!          pagaron con tarjeta de débito  respecto al total de personas en la lista.
    #! 4) - Cuál es el total de descuentos en pesos que aplicó la empresa, pero solo de 
    #!          los aplicados a tarjetas de crédito
    #! 5) - El nombre y la edad de la persona que pagó el precio más alto por una entrada de 
    #!          tipo "General" y pagó con tarjeta de débito (Solo la primera que se encuentre)
    #! 6) - La cantidad de personas que compraron entradas de tipo "Platea" y cuya 
    #!          edad es un número primo.
    #! 7) - Calcula el monto total recaudado por la venta de entradas de tipo "Platea" y 
    #!          pagadas con tarjeta de debito por personas cuyas edades son múltiplos de 6.
'''

#ANTES DE CARGA

nombre_comprador = 0 
edad = 0 
genero = 0 
tipo_entrada = 0 
medio_pago = 0 
precio_entrada = 0
contador_total = 0

contador_campo_masc = 0
contador_campo_fem = 0
contador_campo_otro = 0

contador_general_credito = 0
suma_edad_general_credito = 0 
promedio_edad_general_credito = 0

contador_platea_debito = 0
porcentaje_platea_debito = 0

contador_campo_credito = 0
contador_platea_credito = 0
total_descuentos_credito = 0

bandera = True
max_precio_general_debito = 0
nombre_max_precio_general_debito = ""
edad_max_precio_general_debito = 0

contador_divisores = 0
contador_platea_edad_primo = 0

monto_recaudado_platea_deb_mult_6 = 0 

#CARGA DE DATOS

while True:
    print
    ingreso = input("Desea ingresar la compra?")

    if ingreso == "no": 
        break
    
    #NOMBRE
    nombre_comprador = input("Ingresar nombre: ")

    #EDAD
    edad = input("Ingresar edad: ")

    while int(edad) <16:
        edad = input("Ingresar edad: ")
    
    edad = int(edad)

    #GENERO
    genero = input("Ingresar genero: ")

    while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
        genero = input("Ingresar genero: ")

    #Tipo de Entrada
    tipo_entrada = input("Ingresar tipo de entrada: ")
    
    while tipo_entrada != "General" and tipo_entrada != "Campo delantero" and tipo_entrada != "Platea":
        tipo_entrada = input("Ingresar tipo de entrada: ")

    #Medio de pago
    medio_pago = input("Ingresar medio de pago: ")

    while medio_pago != "Crédito" and medio_pago != "Efectivo" and medio_pago != "Débito":
        medio_pago = input("Ingresar medio de pago: ")
    
    contador_total +=1

    #Precio entrada
    match tipo_entrada:
        case "General":
            match medio_pago:
                case "Crédito": 
                    precio_entrada = 16000*0.8 
                    #! 2) - Determina cuántas personas compraron entradas de tipo "General" pagando con tarjeta de crédito y su edad promedio.
                    contador_general_credito += 1    #! 4) - Cuál es el total de descuentos en pesos que aplicó la empresa, pero solo de los aplicados a tarjetas de crédito
                    suma_edad_general_credito += edad
                case "Débito":
                    precio_entrada = 16000*0.85
                        #! 5) - El nombre y la edad de la persona que pagó el precio más alto por una entrada de tipo "General" y pagó con tarjeta de débito (Solo la primera que se encuentre)
                    if bandera or max_precio_general_debito<precio_entrada:
                        max_precio_general_debito = precio_entrada
                        nombre_max_precio_general_debito = nombre_comprador
                        edad_max_precio_general_debito = edad
                        bandera = False

                case "Efectivo":
                    precio_entrada = 16000
        case "Campo delantero":
            match medio_pago:
                case "Crédito":
                    precio_entrada = 25000*0.8
                    #! 4) - Cuál es el total de descuentos en pesos que aplicó la empresa, pero solo de los aplicados a tarjetas de crédito
                    contador_campo_credito += 1
                case "Débito":
                    precio_entrada = 25000*0.85
                case "Efectivo":
                    precio_entrada = 25000
            match genero: #! 1) - Determina el género más frecuente entre las personas que compraron entradas de tipo "Campo".
                case"Masculino":
                    contador_campo_masc += 1
                case "Femenino" :
                    contador_campo_fem += 1
                case "Otro":
                    contador_campo_otro += 1
        case "Platea":
            #! 6) - La cantidad de personas que compraron entradas de tipo "Platea" y cuya edad es un número primo.
            
            for i in range (1,edad+1):
                contador_divisores = 0

                if edad % i == 0:
                    contador_divisores += 1
            
            if contador_divisores <=2:
                contador_platea_edad_primo += 1

            match medio_pago:
                case "Crédito":
                    precio_entrada = 30000*0.8
                    #! 4) - Cuál es el total de descuentos en pesos que aplicó la empresa, pero solo de los aplicados a tarjetas de crédito
                    contador_platea_credito += 1
                case "Débito": 
                    precio_entrada = 30000*0.85
                    #! 3) - Calcula el porcentaje de personas que compraron entradas de tipo "Platea" y pagaron con tarjeta de débito  respecto al total de personas en la lista.
                    contador_platea_debito +=1
                    #! 7) - Calcula el monto total recaudado por la venta de entradas de tipo "Platea" y pagadas con tarjeta de debito por personas cuyas edades son múltiplos de 6.
                    if edad % 6 == 0:
                        monto_recaudado_platea_deb_mult_6 += precio_entrada
                case "Efectivo":
                    precio_entrada = 30000


#DESPUES DE CARGA
    #! 1) - Determina el género más frecuente entre las personas que compraron entradas de tipo "Campo".
if contador_campo_fem == 0 and contador_campo_masc == 0 and contador_campo_otro == 0:
    mensaje = "No se compraron entradas de campo"
elif contador_campo_masc > contador_campo_fem and contador_campo_masc > contador_campo_otro:
    mensaje = f"La mayoría que compro campo es Masculino, con un total de {contador_campo_masc} compradas."
elif contador_campo_fem > contador_campo_otro: 
    mensaje = f"La mayoría que compro campo es Femenino, con un total de {contador_campo_fem} compradas."
else: 
    mensaje = f"La mayoría que compro campo es Otro, con un total de {contador_campo_otro} compradas."

print("----------------------------------")
print(mensaje)

    #! 2) - Determina cuántas personas compraron entradas de tipo "General" pagando con tarjeta 
    #!          de crédito y su edad promedio.

if contador_general_credito == 0:
    mensaje = "No hubo compradores"
else:
    promedio_edad_general_credito = suma_edad_general_credito/contador_general_credito
    mensaje = f"Cantidad de personas que compraron entrada General cpn tarjeta de crédito: {contador_general_credito}\nEl promedio de edades es: {promedio_edad_general_credito}"

print("----------------------------------")
print (mensaje)

    #! 3) - Calcula el porcentaje de personas que compraron entradas de tipo "Platea" y 
    #!          pagaron con tarjeta de débito  respecto al total de personas en la lista.

print("----------------------------------")

porcentaje_platea_debito = (contador_platea_debito*100)/contador_total

print(f"EL porcentaje de personas que compraron Platea con tarjeta de Débito es: {porcentaje_platea_debito}%")

    #! 4) - Cuál es el total de descuentos en pesos que aplicó la empresa, pero solo de los aplicados a tarjetas de crédito

total_descuentos_credito = (contador_campo_credito*16000*0.2) + (contador_general_credito*0.8*25000) + (contador_platea_credito*0.2*30000)

print("----------------------------------")
print(f"El total de descuentos en pesos con tarjeta de crédito es: {total_descuentos_credito}$")

    #! 5) - El nombre y la edad de la persona que pagó el precio más alto por una entrada de 
    #!          tipo "General" y pagó con tarjeta de débito (Solo la primera que se encuentre)

print("----------------------------------")
print (f"La persona que mas pago por una entrada general es: {nombre_max_precio_general_debito}, de {edad_max_precio_general_debito} años.\nEl total abonado es de: {max_precio_general_debito}$")
    
    #! 6) - La cantidad de personas que compraron entradas de tipo "Platea" y cuya 
    #!          edad es un número primo.

print("----------------------------------")
print(f"La cantidad de personas que compraron Platea y su edad es un número primo es: {contador_platea_edad_primo}")

    #! 7) - Calcula el monto total recaudado por la venta de entradas de tipo "Platea" y 
    #!          pagadas con tarjeta de debito por personas cuyas edades son múltiplos de 6.

print("----------------------------------")
print(f"Total reacudado por personas cuya edad es múltiplo de 6 y compraron Platea con Débito: {monto_recaudado_platea_deb_mult_6}")
print("----------------------------------")