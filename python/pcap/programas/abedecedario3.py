abedecedarios = [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
    "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]

resultado = [letra for i, letra in enumerate(abedecedarios) if(i + 1)% 3 != 0]
print("Lista del abedecedarion sin los multiples de tres. ")
print(resultado)