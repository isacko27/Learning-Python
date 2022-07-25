lista = ['a','b','c']


for item in lista:
    print(lista.index(item),item)

for item in enumerate(lista):
    print(item)

for indice,item in enumerate(lista):
    print(indice,item)

print("\n")

for indice,item in enumerate(range(1,10)):
    print(indice,item)

mis_tuples = list(enumerate(lista))
print(mis_tuples)
