import math
x = float(input("Ingresa un número: "))
try:
    assert x >= 0.0
except AssertionError:
    print("numero menor de cero")
    exit(1)

print(x)   
x = math.sqrt(x)
print("Fin")


