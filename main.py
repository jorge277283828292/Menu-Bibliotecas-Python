#Este programa se trata sobre un menu de opciones en distintas bibliotecas de python
from opcions import informacion
from prog_random.adivinar import adivinar
from prog_datatime.edades import calcular_edad
from prog_calendar.dias import mostrar_meses

while True:
    #Posibles Opciones
    try:
        informacion()
        eleccion = input("¿Cual bibilioteca desea utilizar?")

        match eleccion:
            #calendar
            case "1":
                mostrar_meses()
            #datatime
            case "2":
                calcular_edad()
            #os
            case "3":
                pass
            #json
            case "4":
                pass
            #math
            case "5":
                pass
            #secrets
            case "6":
                pass
            #random
            case "7":
                adivinar()
            #re
            case "8":
                pass
            #statistics
            case "9":
                pass
            #time
            case "10":
                pass
            #exit
            case "11":
                break

    except KeyboardInterrupt:
        print("\n¡Programa terminado por el usuario (Ctrl+C)! ¡Hasta luego!")
        break
    except EOFError:
        print("\n¡Programa terminado por fin de entrada (EOF)! ¡Hasta luego!")
        break
