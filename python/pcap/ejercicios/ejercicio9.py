import random

numero_secreto = random.randint(1, 100)
intentos = 0

while True:
    intento = int(input("Adivina el número (1-100): "))
    intentos += 1
    if intento < numero_secreto:
        print("Demasiado bajo.")
    elif intento > numero_secreto:
        print("Demasiado alto.")
    else:
        print("¡Correcto! Lo adivinaste en", intentos, "intentos.")
        break
