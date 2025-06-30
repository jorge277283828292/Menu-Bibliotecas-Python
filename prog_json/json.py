import json
import time

def programa_json():
    #Opciones multiples para la modificaciones, edicion o eliminacion de un documento formato JSON.
    #Multiple options for modifying, editing, or deleting a JSON document.
    while True: # Añadido: Bucle para mantener el menú JSON activo
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
            except json.JSONDecodeError: # Añadido para manejar JSON mal formado/vacío
                print("Error: El archivo no es un JSON válido o está vacío.")

        elif opcion == "3":
            try:
                with open("datos.json", "r+") as archivo: # Cambiado a r+ para leer y escribir
                    datos = json.load(archivo)

                clave = input("Ingresa la clave que deseas modificar: ")
                if clave in datos: # Añadido: Verificar si la clave existe
                    valor = input("Ingresa el nuevo valor: ")
                    datos[clave] = valor

                    archivo.seek(0) # Mover el puntero al inicio para reescribir
                    json.dump(datos, archivo, indent=4)
                    archivo.truncate() # Recortar si el nuevo contenido es más corto

                    print("Archivo JSON modificado con éxito.")
                else:
                    print(f"La clave '{clave}' no existe en el archivo JSON.")
            except FileNotFoundError:
                print("El archivo JSON no existe.")
            except json.JSONDecodeError: # Añadido para manejar JSON mal formado/vacío
                print("Error: El archivo no es un JSON válido o está vacío.")


        elif opcion == "4":
            try:
                with open("datos.json", "r+") as archivo: # Cambiado a r+ para leer y escribir
                    datos = json.load(archivo)

                clave = input("Ingresa la clave que deseas agregar: ")
                valor = input("Ingresa el valor: ")

                datos[clave] = valor

                archivo.seek(0) # Mover el puntero al inicio para reescribir
                json.dump(datos, archivo, indent=4)
                archivo.truncate() # Recortar si el nuevo contenido es más corto

                print("Datos agregados con éxito.")
            except FileNotFoundError:
                print("El archivo JSON no existe.")
            except json.JSONDecodeError: # Añadido para manejar JSON mal formado/vacío
                print("Error: El archivo no es un JSON válido o está vacío.")

        elif opcion == "5":
            print("Saliendo del programa JSON...")
            break # Este break ahora sí rompe el 'while True' de programa_json()
        else:
            print("Opción inválida. Por favor, intenta de nuevo.")

        #Tiempo de espera.
        #Waiting time.
            print("Volviendo al menú en 3 segundos...")
            time.sleep(3)