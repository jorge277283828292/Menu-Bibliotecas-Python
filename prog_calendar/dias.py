import calendar
import time

#Muestra el calendario de todos los meses que el usuario ingrese.
#Show the calendar for all the months the user enters.
def mostrar_meses():
    year = int(input("Ingrese el año: "))
    for mes in range(1,13):
        print(calendar.month(year, mes))
        print("\n")

    #Tiempo de espera.
    #Waiting time.
    print("Volviendo al menú en 3 segundos...")
    time.sleep(3)