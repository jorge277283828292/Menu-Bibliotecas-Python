import time

def tiempo():
    #Eleccion de tiempo.
    #Choice the time.
    segundos = int(input("¿Cuánto tiempo deseas ingresar? "))
    #Eleccion de modo
    opcion = input("¿Quieres que el tiempo vaya normal o reversa? (1 = Normal, 2 = Reversa): ")

    #Si es reloj normal.
    #If is a normal watch.
    if opcion == "1":
        for i in range(0, segundos + 1):
            print(i)
            time.sleep(1)

    #Si es reloj en reversa.
    #If is a reverse watch.
    elif opcion == "2":
        for i in range(segundos, 0, -1):
            print(i)
            time.sleep(1)

    else:
        print("¡Opción inválida!")

    #Tiempo de espera.
    #Waiting time.
    print("Volviendo al menú en 3 segundos...")
    time.sleep(3)