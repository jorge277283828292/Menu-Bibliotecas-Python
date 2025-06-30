import time

def tiempo():
    #Eleccion de tiempo
    segundos = int(input("¿Cuánto tiempo deseas ingresar? "))
    #Eleccion de modo
    opcion = input("¿Quieres que el tiempo vaya normal o reversa? (1 = Normal, 2 = Reversa): ")

    #Si es reloj normal
    if opcion == "1":
        for i in range(0, segundos + 1):
            print(i)
            time.sleep(1)

    #Si es reloj en reversa
    elif opcion == "2":
        for i in range(segundos, 0, -1):
            print(i)
            time.sleep(1)

    else:
        print("¡Opción inválida!")

    print("Volviendo al menú en 3 segundos...")
    time.sleep(3)