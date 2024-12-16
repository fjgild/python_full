numero_secreto = 7
intento = int(input("Adivina el número (1-10): "))
if intento == numero_secreto:
    print("¡Correcto!")
else:
    print("Incorrecto. El número era", numero_secreto)
