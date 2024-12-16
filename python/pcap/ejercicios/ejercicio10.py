import random

opciones = ["piedra", "papel", "tijera"]

while True:
    eleccion_usuario = input("Elige piedra, papel o tijera: ").lower()
    eleccion_maquina = random.choice(opciones)
    print("La máquina eligió:", eleccion_maquina)

    if eleccion_usuario == eleccion_maquina:
        print("¡Es un empate!")
    elif (eleccion_usuario == "piedra" and eleccion_maquina == "tijera") or \
         (eleccion_usuario == "papel" and eleccion_maquina == "piedra") or \
         (eleccion_usuario == "tijera" and eleccion_maquina == "papel"):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")

    jugar_de_nuevo = input("¿Quieres jugar de nuevo? (sí/no): ").lower()
    if jugar_de_nuevo != "sí":
        break
