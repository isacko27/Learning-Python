monedas = 5

while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas -= 1
else:print("No tengo mas monedas pibe")

nombre = input("tu nombre: ")

for letra in nombre:
    if letra == 'r':
        break
    print(letra)