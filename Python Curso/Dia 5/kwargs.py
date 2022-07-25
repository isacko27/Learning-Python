def suma(**kwargs): #**KWARGS devuelve un diccionario con los valores dados

    total = 0

    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor
    return total

print(suma(x=3, y=5, z=2))