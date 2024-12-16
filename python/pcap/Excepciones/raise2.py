def mal_asunto(n):
    try:
        return n / 0
    except:
        print("Lo hice otra vez")
        raise ValueError
try:
    mal_asunto(0)
except ValueError:
    print("Error de valor")
except ArithmeticError:
    print("ya veo")
    exit(0)

print("Fin")