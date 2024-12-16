frase = input("introduce frase: ")

frase2 = (frase.lower()).replace('','')

if frase2 == frase2[::-1]:
    print("Es un palindromo")
else:
    print("no es un palindromo")
