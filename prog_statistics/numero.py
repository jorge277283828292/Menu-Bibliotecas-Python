import statistics
import time

def calcular_estadisticas():
    #Agrager lista de numeros para ser separados.
    #Add list of numbers to be separated.
    numeros = input("Ingresa una lista de números separados por comas: ")
    try:
        numeros = [float(x) for x in numeros.split(",")]
        if len(numeros) == 0:
            print("No se ingresaron números.")
            return
    except ValueError:
        print("Error al convertir los números. Por favor, intenta de nuevo.")
        return
    
    #Calculo de estadistitcas.
    #Calculate the estadistics.
    media = statistics.mean(numeros)
    mediana = statistics.median(numeros)
    moda = statistics.mode(numeros) if len(set(numeros)) != len(numeros) else "No hay moda única"
    desviacion_estandar = statistics.stdev(numeros) if len(numeros) > 1 else "No se puede calcular la desviación estándar con menos de 2 números"
    varianza = statistics.variance(numeros) if len(numeros) > 1 else "No se puede calcular la varianza con menos de 2 números"

    #Resultado de estadisticas.
    #Result the estaistics.
    print(f"Media: {media}")
    print(f"Mediana: {mediana}")
    print(f"Moda: {moda}")
    print(f"Desviación estándar: {desviacion_estandar}")
    print(f"Varianza: {varianza}")

    print("Volviendo al menú en 3 segundos...")
    time.sleep(3)