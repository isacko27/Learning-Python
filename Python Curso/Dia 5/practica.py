def reducir_lista(list):
    list.sort()
    list.pop()
    result = []
    for el in list:
        if el not in result:
            result.append(el)
    return result

def promedio(list):
    reduced = reducir_lista(list)
    mean = sum(reduced) / float(len(data))
    return mean

lista_numeros = [1, 5, 34, 62, 12]

print(reducir_lista(lista_numeros))
print(promedio(lista_numeros))
