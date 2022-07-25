from random import shuffle

#lista inicial
palitos = ['-', '--', '---', '----']

#mezclar palitos

def mezclar(lista):
    shuffle(lista)
    return lista

#pedirle intento
def probar_suerte():
    intento = ''
    while intento not in ['1', '2', '3', '4']:
        intento = input("Elige un numero del 1 al 4: ")
    return( int(intento))


#comprobar intento

def chequear_intento(lista,intento):
    match lista[intento -1]:
        case '-':
            print("A lavar los platos pete")

        case _:
            print("Te has salvado brother")

    print(f"Te ha tocado {lista[intento-1]}")

palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados,seleccion)