asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

notas = {}

for asignatura in asignaturas:
    while True:
        try:
            nota = float(input(f"Introduce la nota de {asignatura}: "))
            if 0 <= nota <= 10:
                notas[asignatura] = nota
                break
            else:
                print("Por favor, introduce una nota válida entre 0 y 10.")
        except ValueError:
            print("Por favor, introduce un número válido.")

asignaturas_repetir = [asignatura for asignatura in asignaturas if notas[asignatura] < 5]

if asignaturas_repetir:
    print("Tienes que repetir las siguientes asignaturas:")
    for asignatura in asignaturas_repetir:
        print(asignatura)
else:
    print("¡Felicidades! Has aprobado todas las asignaturas.")
