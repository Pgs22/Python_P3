
###########Condicionales y operaciones básicas

#Ejercicio 1
#Pide un número y muestra un mensaje de bienvenida si el valor es múltiplo de 2 o mayor que 20.
numero = int(input("Escribe un número: "))
multiplo = numero % 2
if(multiplo == 0 or numero > 20):
    print("Bienvenido")

#Ejercicio 2
#Crea un programa que reciba un número del 1 al 4 y devuelva el día de la semana correspondiente: 
# 1 lunes, 2 martes, 3 miércoles, 4 jueves.
import random
numero = (random.randrange(1, 5))
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
def ejercicio3():
    numero1 = int(input("Escribe el primer número: "))
    numero2 = int(input("Escribe el segundo número: "))
    numero3 = int(input("Escribe el tercer número: "))
    #•cuál es el mayor
    if(numero1 > numero2 and numero1 > numero3):
        print("El número más alto es el número 1: ", numero1)
    elif(numero2 > numero3):
        print("El número más alto es el número 2: ", numero2)
    elif(numero2 < numero3):
        print("El número más alto es el número 3: ", numero3)


    #•cuál es el menor
    if(numero1 < numero2 and numero1 < numero3):
        print("El número menor es el número 1: ", numero1)
    elif(numero2 < numero3):
        print("El número menor es el número 2: ", numero2)
    elif(numero2 > numero3):
        print("El número menor es el número 3: ", numero3)


    #•cuántos números se repiten
    count = int(0)
    if(numero1 == numero2):
        count += 1
    if(numero2 == numero3):
        count += 1
    if(numero3 == numero1):
        count += 1
    print(count)

#Ejercicio 4
#Pide tres números y muéstralos ordenados de mayor a menor.
def ejercicio4():
    numero1 = int(input("Escribe el primer número: "))
    numero2 = int(input("Escribe el segundo número: "))
    numero3 = int(input("Escribe el tercer número: "))
    lista = [numero1, numero2, numero3]
    ordenados = sorted(lista, reverse=True)
    print(ordenados)

#Ejercicio 5
#Pide un número y multiplícalo por 3 sin usar el operador de multiplicación, utilizando sumas sucesivas.
num = int(input("Escribe un número: "))
suma = 0
for i in range(3):
    suma += num
print(suma)


###########Bucles y validación de datos

#Ejercicio 6
#Pide dos números enteros y multiplícalos sin usar el operador de multiplicación, utilizando sumas y bucles.
def ejercicio6():
    resultado = 0
    entero1 = int(input("Escribe el primer número: "))
    entero2 = int(input("Escribe el segundo número: "))
    for i in range(entero1):
        resultado += entero2
    print(resultado)

#Ejercicio 7
#Pide un número repetidamente hasta que el usuario introduzca un valor decimal válido 
# comprendido entre 0 y 10.
decimalValido = False
while decimalValido:
    decimal = float(input("Escribe el primer número: "))
    if(decimal >= 0 AND decimal <= 10):
        decimalValido = True
    else:
        decimalValido = False

#Ejercicio 8
#Define un número entero entre 0 y 10 y pide al usuario que intente adivinarlo.
#Si falla, vuelve a pedirlo.
#Si acierta, muestra el número y el total de intentos.
import random
numero = (random.randrange(0, 11))
bingo = False
while bingo:
    numeroUsuario = int(input("Intenta adivinar el número (Pista: El número es entre 0 y 10: "))
    if(numero == numeroUsuario):
        bingo = True
    else:
        bingo = False

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

def menu(opcion):
    match opcion:
        case 1:
            return "Operación 1" + " Multiplicar dos números indicados por el usuario sin usar el operador de multiplicación."
        case 2:
            return "Operación 2" + " Determinar el número mayor y el menor de un grupo de números introducidos por el usuario."
        case 3:
            return "Operación 3" + " Mostrar los números pares."
        case 4:
            return "Operación 4" + " Mostrar la media de los números introducidos."

finalizarPrograma = True
while finalizarPrograma: #Ejecuta el While mientras sea true
    menu(opcion)
    opcion = int(input("Elige una opción del 1 al 4 (0 para salir): "))
    if opcion == 0:
        print("Programa finalizado")
        finalizarPrograma = False
    if opcion <= 4:
        def operacion(opcion):
            match opcion:
                case 1:
                    ejercicio6()
                case 2:
                    ejercicio3()
                case 3:
                    ejercicio4()
                case 4:
                    ejercicio6()

    menu(opcion)


