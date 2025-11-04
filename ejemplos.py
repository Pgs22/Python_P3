#Ejercicio 4
#Pide tres números y muéstralos ordenados de mayor a menor.
lista = []
for i in range(3):
    numero = int(input(f"Escribe el número {i + 1}: "))
    lista.append(numero)
ordenados = sorted(lista, reverse=True)