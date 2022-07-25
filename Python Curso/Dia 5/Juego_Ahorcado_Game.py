#Ahorcado
#Se elije una palabra secreta
#Se muestran guinoes con la cantidad de letras que tiene la palabra _________
#Debera elegir una letra, si esta se encuentra, se mostrara en que lugares esta esa letra   __a___a
#Si esta no se encuentra el jugador perdera una vida  6 vidas
# si vidas = 0 antes de encontrar la palabra pierda else gana

from random import choice

palabras = "humanidad humano persona gente hombre mujer bebe niño niña adolescente adulto adulta anciano anciana don doña señor señora caballero dama individuo trasero culo cola gluteos abdomen hígado músculo cuello corazón mente espíritu pecho cintura cadera espalda sangre carne piel resfriado gripe diarrea salud enfermedad"

def ordenar(text):
    lista = text.split(" ")
    return lista

palabras_lista = ordenar(palabras)


# Definimos la palabra secreta y el espaciodo _________
def random_word(lista):
    #Elegimos la palabra y la ponemos en miniscula
    secret = list(choice(lista).lower())
    spaced = []

    for let in secret:
        spaced.append('_')

    return (secret,spaced)

def revelar(intento, word, encountered):
    index = 0
    revelado = encountered

    for let in word:
        if intento == let:
            revelado[index] = intento
        index += 1

    return revelado

def gana(lista):
    if '_' not in lista:
        return True


def juega(palabras):
    vidas = 6
    win = False
    word, spaced = random_word(palabras)
    revelado = spaced
    print("\t"''.join(spaced))

    while (vidas > 0) and (not win):
        intento = input("""
******************
Dime una letra: """).lower()

        if len(intento) <= 1:

            if intento in revelado:
                print("Ya encontraste esta Letra antes")

            elif intento in word:
                print(f"""
******************               
Bien! encontraste '{intento}'
Vidas: {vidas} """)
                revelado = revelar(intento,word,revelado)
                print("\t"''.join(revelado).upper())

                if gana(revelado):
                    print(f"""
======================================>              
    Has adivinado la palabra es 
    '{''.join(word).upper()}'
    Felicidades!
======================================>
                    """)
                    win = True

            else:
                vidas -= 1
                print(f"""
******************               
Perdiste una vida! '{intento}'
Vidas: -{vidas}""")
                print("\t"''.join(revelado).upper())

        else:
            print("Solo puedes poner una letra pete")

        if win:
            restart = input("Felicidades Quieres volver a jugar?(y/n)").lower()

            if restart == 'y' or restart == 'yes':
                juega(palabras)

            else:
                print('Gracias Por jugar!')
                break

        if vidas == 0:
            print(f"""
======================================>              
    Perdiste :CC la palabra era
    '{''.join(word).upper()}'
    Suerte la proxima
======================================>
""")

            restart = input("Quieres volver a jugar?(y/n)").lower()

            if restart == 'y' or restart == 'yes':
                juega(palabras)




juega(palabras_lista)






