mi_lista = ['g','o','a','r','p','k']
mi_lista2 = ['d','e','f']
mi_lista3 = mi_lista + mi_lista2

mi_lista3.append('g')
print(mi_lista3)
eliminado = mi_lista3.pop(2)
print(mi_lista)
mi_lista.sort()
print(mi_lista)
print(mi_lista3)
print(eliminado)