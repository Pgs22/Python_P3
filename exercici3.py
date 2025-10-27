
###########Condicionales y operaciones básicas

#Ejercicio 1
#Pide un número y muestra un mensaje de bienvenida si el valor es múltiplo de 2 o mayor que 20.
import math
numero = float(input("Escribe un número: "))
multiplo = numero % 2
if(multiplo == 0):
    print()
else(numero > 20):
    print()



#Ejercicio 2
#Crea un programa que reciba un número del 1 al 4 y devuelva el día de la semana correspondiente: 
# lunes, 2 martes, 3 miércoles, 4 jueves.

#Ejercicio 3
#Pide tres números y determina:
#•cuál es el mayor
#•cuál es el menor
#•cuántos números se repiten

#Ejercicio 4
#Pide tres números y muéstralos ordenados de mayor a menor.

#Ejercicio 5
#Pide un número y multiplícalo por 3 sin usar el operador de multiplicación, utilizando sumas sucesivas.


###########Bucles y validación de datos

#Ejercicio 6
#Pide dos números enteros y multiplícalos sin usar el operador de multiplicación, utilizando sumas y bucles.

#Ejercicio 7
#Pide un número repetidamente hasta que el usuario introduzca un valor decimal válido 
# comprendido entre 0 y 10.

#Ejercicio 8
#Define un número entero entre 0 y 10 y pide al usuario que intente adivinarlo.
#Si falla, vuelve a pedirlo.
#Si acierta, muestra el número y el total de intentos.

###########Funciones y control de operaciones

#Ejercicio 9
#Desarrolla un programa que permita al usuario elegir entre diferentes operaciones mediante un número del 1 al 4.
#•El programa solo finalizará si se elige la opción 0.
#•Después de realizar la operación seleccionada, se deben mostrar nuevamente las opciones.
#•Operaciones disponibles:
#oMultiplicar dos números indicados por el usuario sin usar el operador de multiplicación.
#oDeterminar el número mayor y el menor de un grupo de números introducidos por el usuario.
#oMostrar los números pares.
#oMostrar la media de los números introducidos.