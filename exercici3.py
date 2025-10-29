
###########Condicionales y operaciones básicas

#Ejercicio 1
#Pide un número y muestra un mensaje de bienvenida si el valor es múltiplo de 2 o mayor que 20.
numero = float(input("Escribe un número: "))
multiplo = numero % 2
if(multiplo == 0 or numero > 20):
    print("Bienvenido")

#Ejercicio 2
#Crea un programa que reciba un número del 1 al 4 y devuelva el día de la semana correspondiente: 
# lunes, 2 martes, 3 miércoles, 4 jueves.
numero = input("Escribe un número: ")
match numero:
    case 1:
        print("lunes")
    case 2:
        print("martes")
    case 3:
        print("miércoles")
    case 4:
        print("jueves")

#Ejercicio 3
#Pide tres números y determina:
numero1 = input("Escribe el primer número: ")
numero2 = input("Escribe el segundo número: ")
numero3 = input("Escribe el tercer número: ")
#•cuál es el mayor
if(numero1 > numero2 and numero1 > numero3):
    print("El número más alto es el número 1: ", numero1)
elif(numero2 > numero3):
    print("El número más alto es el número 2: ", numero2)
else:
    print("El número más alto es el número 3: ", numero3)

#•cuál es el menor
if(numero1 < numero2 and numero1 < numero3):
    print("El número menor es el número 1: ", numero1)
elif(numero2 < numero3):
    print("El número menor es el número 2: ", numero2)
else:
    print("El número menor es el número 3: ", numero3)

#•cuántos números se repiten
count = 0
if(numero1 == numero2):
    count+= 1
elif(numero2 == numero3):
    count+= 1
elif(numero3 == numero1):
    count+= 1
print(count)

#Ejercicio 4
#Pide tres números y muéstralos ordenados de mayor a menor.
numero1 = input("Escribe el primer número: ")
numero2 = input("Escribe el segundo número: ")
numero3 = input("Escribe el tercer número: ")
lista = [numero1, numero2, numero3]
ordenados = sorted(lista)

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