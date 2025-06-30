import re
import time

def buscador_texto():
    #Crea un texto y da la opcion para buscar una palabra clave de este.
    texto = input("Ingresa el texto en el que deseas buscar: ")
    patron = input("Ingresa el patrón de búsqueda (puedes utilizar expresiones regulares): ")
    
    #Manejo de excepciones.
    try:
        resultados = re.findall(patron, texto)
        if resultados:
            print(f"Se encontraron {len(resultados)} coincidencias:")
            for i, resultado in enumerate(resultados, start=1):
                print(f"{i}. {resultado}")
        else:
            print("No se encontraron coincidencias.")
    except re.error as e:
        print(f"Error en la expresión regular: {e}")

    print("Volviendo al menú en 3 segundos...")
    time.sleep(3)