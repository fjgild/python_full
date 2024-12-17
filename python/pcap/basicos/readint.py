def read_int(prompt, min, max):
      while True:
        try:
            value = int(input(prompt))
            if min <= value <= max:
                return value
            else:
                print("Error número inválido.")
        except ValueError:
            print("Valor no valido.")

v = read_int("Ingresa un número entre -10 a 10: ", -10, 10)

print("El número es:", v)