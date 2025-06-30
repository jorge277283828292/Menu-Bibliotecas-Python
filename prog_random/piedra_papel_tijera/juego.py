# Juego de Piedra, Papel o Tijera. El que gane 3 veces gana la partida.
import random
import time

def juego():
    elecciones = ["piedra", "papel", "tijera"]
    victorias_usuario = 0
    victorias_computadora = 0

    while True:
        print("="*50)
        print("Juego de Piedra, Papel o Tijera contra la computadora")
        print("¡El que gane 3 veces se lleva la victoria!")
        usuario = input("Elije tu jugada [Piedra] [Papel] [Tijera]: ").lower()
        print("="*50)
        print()

        #Si la respuesta no es "Piedra", "Papel" o "Tijera".
        #If the answer isn't "Stone", "Paper", "Scissor".
        if usuario not in elecciones:
            print("Elección inválida, no se puede usar esa jugada.")
            continue

        computadora = random.choice(elecciones)
        print(f"La computadora eligió: {computadora}")

        #Los posibles resultados.
        #The possibles results.
        if usuario == computadora:
            resultado = "Empate"
        elif (usuario == "piedra" and computadora == "tijera") or \
             (usuario == "papel" and computadora == "piedra") or \
             (usuario == "tijera" and computadora == "papel"):
            resultado = "Ganaste"
            victorias_usuario += 1
        else:
            resultado = "Perdiste"
            victorias_computadora += 1

        #Recuento del marcador.
        #Count the marker.
        print(f"{resultado}! | Marcador -> Computadora: {victorias_computadora}, Usuario: {victorias_usuario}")
        print("-"*80)

        #Si el usuario gana.
        #If users win.
        if victorias_usuario == 3:
            print("¡La victoria es tuya! 🏆")
            print(f"Marcador final -> Computadora: {victorias_computadora}, Usuario: {victorias_usuario}")
            print("Volviendo al menú en 3 segundos...")
            time.sleep(3)
            break

        #Si la computadora gana.
        #If the computers win.
        elif victorias_computadora == 3:
            print("¡La computadora se ha llevado la victoria! 😢")
            print(f"Marcador final -> Computadora: {victorias_computadora}, Usuario: {victorias_usuario}")
            print("Volviendo al menú en 3 segundos...")
            time.sleep(3)
            break
            
    