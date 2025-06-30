import random as r
import string as s
import time

def contras():
    caracteres = ""
    contraseña = []
    usar_letras = False
    usar_numeros = False
    usar_simbolos = False

    texto = """ 
1. Letras
2. Números
3. Símbolos
4. Generar Contraseña
"""

    print("Bienvenido, aquí puedes generar tu contraseña")
    #Dependiendo de el usuario esta va a ser la longitud del programa.
    #Depending on the user, this will be the length of the program.
    try:
        num = int(input("Dame la longitud que deseas que tenga la contraseña: "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        return

    while True:
        print("=" *50)
        print(texto)
        print("=" *50)
        try:
            eleccion = int(input("Elige una opción: "))
        except ValueError:
            print("Por favor, ingresa un número.")
            continue

        if eleccion == 1:
            usar_letras = True
            print("✔ Letras activadas")
        elif eleccion == 2:
            usar_numeros = True
            print("✔ Números activados")
        elif eleccion == 3:
            usar_simbolos = True
            print("✔ Símbolos activados")
        elif eleccion == 4:
            if not (usar_letras or usar_numeros or usar_simbolos):
                print("❌ Tienes que activar al menos una opción antes de generar la contraseña.")
                continue
            
            #Agrega letras.
            #Add letters.
            if usar_letras:
                caracteres += s.ascii_letters
                contraseña.append(r.choice(s.ascii_letters))
            #Agrega numeros.
            #Add numbers.
            if usar_numeros:
                caracteres += s.digits
                contraseña.append(r.choice(s.digits))
            #Agrega simbolos.
            #Add simbols.
            if usar_simbolos:
                caracteres += s.punctuation
                contraseña.append(r.choice(s.punctuation))

            while len(contraseña) < num:
                contraseña.append(r.choice(caracteres))

            r.shuffle(contraseña)
            contraseña_final = ''.join(contraseña)
            print(f"\n🔐 Tu contraseña generada es: {contraseña_final}")
            break
        else:
            print("❌ Opción inválida")

    #Tiempo de espera.
    #Waiting time.
    print("Volviendo al menú en 3 segundos...")
    time.sleep(3)
