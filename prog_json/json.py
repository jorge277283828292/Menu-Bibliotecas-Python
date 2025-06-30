import json
import time
def programa_json():
        #Opciones multiples para la modificaciones, edicion o eliminacion de un documento formato JSON
        print("\nOpciones:")
        print("1. Crear archivo JSON")
        print("2. Leer archivo JSON")
        print("3. Modificar archivo JSON")
        print("4. Agregar datos al archivo JSON")
        print("5. Salir")

        opcion = input("Ingresa una opción: ")

        if opcion == "1":
            datos = {
                "nombre": "Juan",
                "edad": 30,
                "ocupacion": "Desarrollador"
            }

            with open("datos.json", "w") as archivo:
                json.dump(datos, archivo, indent=4)

            print("Archivo JSON creado con éxito.")

        elif opcion == "2":
            try:
                with open("datos.json", "r") as archivo:
                    datos = json.load(archivo)
                    print("Datos del archivo JSON:")
                    for clave, valor in datos.items():
                        print(f"{clave}: {valor}")
            except FileNotFoundError:
                print("El archivo JSON no existe.")

        elif opcion == "3":
            try:
                with open("datos.json", "r") as archivo:
                    datos = json.load(archivo)

                clave = input("Ingresa la clave que deseas modificar: ")
                valor = input("Ingresa el nuevo valor: ")

                datos[clave] = valor

                with open("datos.json", "w") as archivo:
                    json.dump(datos, archivo, indent=4)

                print("Archivo JSON modificado con éxito.")
            except FileNotFoundError:
                print("El archivo JSON no existe.")

        elif opcion == "4":
            try:
                with open("datos.json", "r") as archivo:
                    datos = json.load(archivo)

                clave = input("Ingresa la clave que deseas agregar: ")
                valor = input("Ingresa el valor: ")

                datos[clave] = valor

                with open("datos.json", "w") as archivo:
                    json.dump(datos, archivo, indent=4)

                print("Datos agregados con éxito.")
            except FileNotFoundError:
                print("El archivo JSON no existe.")

        elif opcion == "5":
            print("Saliendo del programa JSON...")
            break
        else:
            print("Opción inválida. Por favor, intenta de nuevo.")

        #Tiempo de espera
        print("Volviendo al menú en 3 segundos...")
        time.sleep(3)