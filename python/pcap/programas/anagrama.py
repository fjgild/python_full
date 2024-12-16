while True:
    text1 = input("Introduce la 1ª palabra: ").upper()
    if not text1.isalpha():
        print("Error: '"+text1+"' no es una cadena alfabética")
        break

    text2 = input("Introduce la 2ª palabra: ").upper()
    if not text2.isalpha():
        print("Error: '"+text2+"' no es una cadena alfabética")
        break
    
    text1_invertido = text1[::-1]
    text2_invertido = text2[::-1]
    
    print(f"Anagrama: {text1_invertido} y {text2_invertido}")
    
    continuar = input("¿Quieres introducir más palabras? (sí/no): ").strip().lower()
    if continuar != "sí":
        break
