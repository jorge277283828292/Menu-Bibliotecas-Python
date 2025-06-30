import re
import time

def buscador_texto():
    #Crea un texto y da la opcion para buscar una palabra clave de este.
    #Creates a text and gives the option to search for a keyword from it.
    texto = input("Ingresa el texto en el que deseas buscar: ")
    patron = input("Ingresa el patrón de búsqueda (puedes utilizar expresiones regulares): ")
    
    #Manejo de excepciones.
    #Drive the exceptions.
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

    #Tiempo de espera.
    #Waiting time.
    print("Volviendo al menú en 3 segundos...")
    time.sleep(3)