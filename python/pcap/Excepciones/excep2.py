try:
    y = 1 / 0
except (ZeroDivisionError, ArithmeticError):
    print("Hubo un problema al hacer la operacion")
except :
    print("¡Problema!")

print("FIN.")
    