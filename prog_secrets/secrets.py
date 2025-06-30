import secrets
import string
import time

def programa_secrets():
    print("Generador de contraseñas y tokens")
    while True:
        #Opciones de generacion de claves a tokens.
        #Token key generation options
        print("\nOpciones:")
        print("1. Generar contraseña")
        print("2. Generar token")
        print("3. Salir")
        
        opcion = input("Ingresa una opción: ")

        #Si es contraseña
        #If is password.
        if opcion == "1":
            try:
                longitud = int(input("Ingresa la longitud de la contraseña: "))
                caracteres = string.ascii_letters + string.digits + string.punctuation
                contraseña = ''.join(secrets.choice(caracteres) for _ in range(longitud))
                print(f"Contraseña generada: {contraseña}")
            except ValueError:
                print("❌ Longitud inválida. Debe ser un número.")

        #Si es token.
        #If is token.
        elif opcion == "2":
            try:
                longitud = int(input("Ingresa la longitud del token: "))
                token = secrets.token_urlsafe(longitud)
                print(f"Token generado: {token}")
            except ValueError:
                print("❌ Longitud inválida. Debe ser un número.")

        elif opcion == "3":
            print("Saliendo del módulo secrets...")
            break
        else:
            print("Opción inválida. Por favor, intenta de nuevo.")

        #Tiempo de espera.
        #Waiting time.
    print("Volviendo al menú en 3 segundos...")
    time.sleep(3)