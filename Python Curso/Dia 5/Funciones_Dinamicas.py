def chequear3_cifras(lista):
    for n in lista:
        if n in range(100,1000):
            return True
        else:
            pass


resultado = chequear3_cifras([154,23,34,23,12])
print(resultado)