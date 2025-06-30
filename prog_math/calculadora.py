import math
import time

def programa_math():
    while True:
        #Calculadora avanzada.
        #Avance calculate.
        print("\nOpciones:")
        print("1. Funciones trigonométricas")
        print("2. Logaritmos")
        print("3. Potencias")
        print("4. Raíces")
        print("5. Salir")

        opcion = input("Ingresa una opción: ")

        if opcion == "1":
            print("Funciones trigonométricas:")
            try:
                angulo = float(input("Ingresa un ángulo en grados: "))
                angulo_radianes = math.radians(angulo)

                seno = math.sin(angulo_radianes)
                coseno = math.cos(angulo_radianes)
                tangente = math.tan(angulo_radianes)

                print(f"Seno de {angulo}°: {seno}")
                print(f"Coseno de {angulo}°: {coseno}")
                print(f"Tangente de {angulo}°: {tangente}")
            except ValueError:
                print("Debes ingresar un número válido.")

        elif opcion == "2":
            print("Logaritmos:")
            try:
                numero = float(input("Ingresa un número: "))
                logaritmo_natural = math.log(numero)
                logaritmo_base_10 = math.log10(numero)

                print(f"Logaritmo natural de {numero}: {logaritmo_natural}")
                print(f"Logaritmo base 10 de {numero}: {logaritmo_base_10}")
            except ValueError:
                print("El número debe ser mayor que 0.")

        elif opcion == "3":
            print("Potencias:")
            try:
                base = float(input("Ingresa la base: "))
                exponente = float(input("Ingresa el exponente: "))
                potencia = math.pow(base, exponente)
                print(f"{base} elevado a la potencia de {exponente}: {potencia}")
            except ValueError:
                print("Debes ingresar números válidos.")

        elif opcion == "4":
            print("Raíces:")
            try:
                numero = float(input("Ingresa un número: "))
                raiz_cuadrada = math.sqrt(numero)
                print(f"Raíz cuadrada de {numero}: {raiz_cuadrada}")
            except ValueError:
                print("Debes ingresar un número válido (mayor o igual a 0).")

        elif opcion == "5":
            print("Saliendo del módulo math...")
            break
        else:
            print("Opción inválida. Por favor, intenta de nuevo.")

        #Tiempo de espera.
        #Waiting time.
        print("Volviendo al menú en 3 segundos...")
        time.sleep(3)