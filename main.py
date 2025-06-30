#Este programa se trata sobre un menu de opciones en distintas bibliotecas de python
from opcions import informacion
from prog_random.adivinar.adivinar import adivinar
from prog_random.generador_contrasenas.generador import contras
from prog_random.piedra_papel_tijera.juego import juego
from prog_random.opciones_random import opciones_random
from prog_datatime.edades import calcular_edad
from prog_calendar.dias import mostrar_meses
from prog_os.carpetas import navegar_carpetas
from prog_json.json import programa_json
from prog_math.calculadora import programa_math
from prog_re.texto import buscador_texto
from prog_secrets.secrets import programa_secrets
from prog_statistics.numero import calcular_estadisticas
from prog_time.cronometro import tiempo

while True:
    #Posibles Opciones
    try:
        informacion()
        eleccion = input("¿Cual bibilioteca desea utilizar? ")

        match eleccion:
            #calendar
            case "1":
                mostrar_meses()
            #datatime
            case "2":
                calcular_edad()
            #os
            case "3":
                navegar_carpetas()
            #json
            case "4":
                programa_json()
            #math
            case "5":
                programa_math()
            #secrets
            case "6":
                programa_secrets()
            #random
            case "7":
                opciones_random()
                eleccion_random = input("¿Cual programa deseas ejecutar?")
                if eleccion_random == "1":
                    adivinar()
                elif eleccion_random == "2":
                    contras()
                elif eleccion_random == "3":
                    juego()
            #re
            case "8":
                buscador_texto()
            #statistics
            case "9":
                calcular_estadisticas()
            #time
            case "10":
                tiempo()
            case "11":
                break

    except KeyboardInterrupt:
        print("\n¡Programa terminado por el usuario (Ctrl+C)! ¡Hasta luego!")
        break
    except EOFError:
        print("\n¡Programa terminado por fin de entrada (EOF)! ¡Hasta luego!")
        break
