mensaje = input("Pon k para kilos y L para libras: ").lower()
mensajePeso = float(input("Pon el peso: "))

if mensaje == 'k':
    mensajeLibras = mensajePeso * 2.2046
    print("El peso en kilos es: " + str(mensajePeso))
    print("El peso en libras es: " + str(mensajeLibras))
elif mensaje == 'l':
    mensajeKilos = mensajePeso * 0.453592
    print("El peso en libras es: " + str(mensajePeso))
    print("El peso en kilos es: " + str(mensajeKilos))
else:
    print("Entrada no válida.")