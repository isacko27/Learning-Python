precios_cafe = [('capuchino',1.5),('expresso',1.2),('Moka',1.9)]

for cafe,elemento in precios_cafe:
    print(cafe)

def cafe_mas_caro(lista):

    precio_mayor = 0
    cafe_mas_caro = ''

    for cafe,precio in lista:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass

    return (cafe_mas_caro,precio_mayor)

print(cafe_mas_caro(precios_cafe))