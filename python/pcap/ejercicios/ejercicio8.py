numero = int(input("Ingresa un número entero positivo: "))
factorial = 1
for i in range(1, numero + 1):
    factorial *= i
print("El factorial de", numero, "es", factorial)
