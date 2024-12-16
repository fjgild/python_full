primitiva = input("introduce los numeros de la primitiva: ")

primitiva = [int(num) for num in primitiva]

if len(primitiva) == 6:
    primitiva.sort()
    print("El numero de la primitiva es: ", primitiva)
else:
    print("numero de loteria no valido")