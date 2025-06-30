import time

def tiempo():
    segundos = int(input("¿Cuánto tiempo deseas ingresar? "))

    opcion = input("¿Quieres que el tiempo vaya normal o reversa? (1 = Normal, 2 = Reversa): ")

    if opcion == "1":
        for i in range(0, segundos + 1):
            print(i)
            time.sleep(1)

    elif opcion == "2":
        for i in range(segundos, 0, -1):
            print(i)
            time.sleep(1)

    else:
        print("¡Opción inválida!")
