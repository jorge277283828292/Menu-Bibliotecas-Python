import os
import time

def navegar_carpetas():
    ruta_actual = os.getcwd()
    print(f"Ruta actual: {ruta_actual}")
    
    while True:
        #Navegador entre carpetas y documentos del computador.
        #Browser between folders and documents on your computer.
        print("\nOpciones:")
        print("1. Listar contenido de la carpeta actual")
        print("2. Cambiar a otra carpeta")
        print("3. Crear una nueva carpeta")
        print("4. Crear un nuevo archivo")
        print("5. Salir")
        
        opcion = input("Ingresa una opción: ")
        
        if opcion == "1":
            contenido = os.listdir()
            print("\nContenido de la carpeta actual:")
            for item in contenido:
                if os.path.isdir(item):
                    print(f"[Carpeta] {item}")
                else:
                    print(f"[Archivo] {item}")
        elif opcion == "2":
            ruta = input("Ingresa la ruta de la carpeta a la que deseas cambiar: ")
            try:
                os.chdir(ruta)
                ruta_actual = os.getcwd()
                print(f"Ruta actual: {ruta_actual}")
            except FileNotFoundError:
                print("La ruta ingresada no existe.")
        elif opcion == "3":
            nombre_carpeta = input("Ingresa el nombre de la carpeta a crear: ")
            try:
                os.mkdir(nombre_carpeta)
                print(f"Carpeta '{nombre_carpeta}' creada con éxito.")
            except FileExistsError:
                print(f"La carpeta '{nombre_carpeta}' ya existe.")
        elif opcion == "4":
            nombre_archivo = input("Ingresa el nombre del archivo a crear: ")
            try:
                with open(nombre_archivo, "w") as archivo:
                    contenido = input("Ingresa el contenido del archivo: ")
                    archivo.write(contenido)
                print(f"Archivo '{nombre_archivo}' creado con éxito.")
            except Exception as e:
                print(f"Error al crear el archivo: {e}")
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Por favor, intenta de nuevo.")
        
        #Tiempo de espera.
        #Waiting time.
        print("Volviendo al menú en 3 segundos...")
        time.sleep(3)