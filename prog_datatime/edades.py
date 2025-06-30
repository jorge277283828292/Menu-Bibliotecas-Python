from datetime import datetime
import time

#Calcula la edad del usuario dependiendo de la fecha de nacimiento.
#Calculates the user's age depending on the date of birth.
def calcular_edad():
    #Ingreso de informacion
    fecha_nacimiento_str = input("Ingresa tu fecha de nacimiento (AAAA-MM-DD): ")
    fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%Y-%m-%d")
    hoy = datetime.today()
    #Calcular edad.
    #Calculate age.
    edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    print(f"Tu edad es: {edad} años")

    #Tiempo de espera.
    #Waiting time.
    print("Volviendo al menú en 3 segundos...")
    time.sleep(3)
