#Pregunta nombre Y lo saluda
#Numero aleatorio entre el 1-100
#8 intentos para adivinarlo
#input de numero y el programa respondera si el numero dicho es mayor o menor al aleatorio
# se permiten numeros mayores a 1 y menores que 100 de 1-100
# Si acierta el numero se informa, y se da el numero de intentos que le tomo llegar ahi
# Si no acierta el juego vuelve a comenzar hasta que gane o hasta que se agoten los 8 intentos

from random import *
nombre = input("Hola! Como te llamas?: ")
num_aleatorio = randint(1,100)

y = input(f"""Mucho gusto {nombre}
He pensado un numero aleatorio para ti, te quiero retar a que lo adivines
Estas listo? (y/n): """).lower()




if y == 'y':

    restart = True

    while restart:

        intentos = int(input("Cuantos intentos quieres?: "))
        fallos = 1

        acertado = False
        print(f"\nCuentas con {intentos} intentos comenzemos")
        for i in range(0,intentos):
            respuesta = int(input("\nDime un numero: "))
            if respuesta == num_aleatorio:
                print("""
            -------------------------
            Has acertado! Felicidades
            -------------------------\n\n""")
                acertado = True
                break
            elif respuesta > num_aleatorio:
                print(f"[{intentos-i}] es menor")
                fallos += 1
                continue
            elif respuesta < num_aleatorio:
                print(f"[{intentos-i}]es mayor")
                fallos += 1
                continue
            elif respuesta < 0 or respuesta > 100 or respuesta == float:
                print(f"[{intentos-i}]Bro es un numero entero entre 1-100 no Exageres")
                fallos += 1
                continue
            else:
                print(f"[{intentos-i}]Eso no es un numero")
                fallos += 1
                continue
        if i == 1:
            print(f"""
            ---------------------------
            Se han acabado los intentos
                    era {num_aleatorio}
               Intentalo nuevamente
            ---------------------------\n""")

        if acertado:
            print(f"Lo lograste en {fallos} intentos!")
            restart = input("Quieres volver a jugar? (y/n):").lower()
            if restart == 'n':
                restart = False
            elif restart == 'y':
                 restart = True
        else: restart = False

    print("Gracias Por Jugar!")

print("TERMINANDO JUEGO...")

