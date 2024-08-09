import random

def jugar():
    opciones = ["piedra", "papel", "tijera"]
    victorias_usuario = 0
    victorias_computadora = 0
    empates = 0
    historial = []

    while True:
        eleccion_usuario = input("Elige piedra, papel o tijera: ").lower().strip()
        if eleccion_usuario not in opciones:
            print("Opción inválida. Por favor, elige piedra, papel o tijera.")
            continue

        eleccion_computadora = random.choice(opciones)
        print(f"La computadora eligió: {eleccion_computadora}")

        if eleccion_usuario == eleccion_computadora:
            print("¡Es un empate!")
            empates += 1
            historial.append(f"Empate: ambos eligieron {eleccion_usuario}")
        elif (eleccion_usuario == "piedra" and eleccion_computadora == "tijera") or \
             (eleccion_usuario == "papel" and eleccion_computadora == "piedra") or \
             (eleccion_usuario == "tijera" and eleccion_computadora == "papel"):
            print("¡Ganaste!")
            victorias_usuario += 1
            historial.append(f"Ganaste: {eleccion_usuario} vence a {eleccion_computadora}")
        else:
            print("Perdiste.")
            victorias_computadora += 1
            historial.append(f"Perdiste: {eleccion_computadora} vence a {eleccion_usuario}")

        jugar_otra_vez = input("¿Quieres jugar otra vez? (sí/no): ").lower().strip()
        if jugar_otra_vez != "sí":
            print("\n--- Resultados Finales ---")
            print(f"Victorias del usuario: {victorias_usuario}")
            print(f"Victorias de la computadora: {victorias_computadora}")
            print(f"Empates: {empates}")
            print("\n--- Historial de juegos ---")
            for juego in historial:
                print(juego)
            print("¡Gracias por jugar!")
            break

# Ejecutar el juego
jugar()
