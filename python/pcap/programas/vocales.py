palabra = input("Introduce una palabara: ")
palabra2 = palabra.lower()
vocales = ["a", "e", "i", "o", "u"]

vocales_en_palabra = [letra for letra in palabra2 if letra in vocales]
cantidad = len(vocales_en_palabra)

print("La cantidad de vocales es: ", cantidad)