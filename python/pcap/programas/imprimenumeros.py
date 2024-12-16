from imprimepares import imprimepares as impp

line = input("Ingresa unos numeros separados por espacios: ")
strings = line.split()
total = 0
try:
    for substr in strings:
        total += float(substr)
    print("El total es:", total)
except:
    print("Error: '" + substr + "' no es un numero.")

print("Los pares son los siguientes numeros:")
impp(strings)