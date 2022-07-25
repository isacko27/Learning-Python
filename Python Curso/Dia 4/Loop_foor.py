lista = ['a','b','c','d']

for letra in lista * 2:
    print(f"Letra numero {lista.index(letra) + 1}: {letra}")