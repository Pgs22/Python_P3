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