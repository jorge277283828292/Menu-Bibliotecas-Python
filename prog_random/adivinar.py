import time
import random

#Genera un numero entre 1 al 10, y el usuario debe adivinar.
def adivinar():
    numeroSecreto = random.randint(1,10)
    intentos = 0
    print("Este juego se trata de adivinar un numero secreto desde el 0 al 10, " \
    "al final el programa te dira cuantos intentos te tomo")

    while True:
        intento = int(input("Adivinar el numero: "))
        intentos = intentos + 1
        
        #Si la respuesta es correcta
        if intento == numeroSecreto:
            print(f"Correcto adivinaste el numero : {numeroSecreto}, en {intentos} intentos.")
            break
        #Si la respuesta es incorrecta
        if not (1 <= intento <= 10):
            print(f"Error, numero de rango invalido")
            continue

    #Tiempo de espera
    print("Volviendo al menú en 3 segundos...")
    time.sleep(3)