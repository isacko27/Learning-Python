def devolver_distintos(num1,num2,num3):

    lista = [num1,num2,num3]
    lista.sort()
    suma = sum(lista)
    if suma >= 15:
        return max(lista)
    elif suma <= 10:
        return  min(lista)
    elif suma < 15 and suma > 10:
        return lista[1]
    else:
        return f"es muy pc pana me da amsiedad {suma}"

print(devolver_distintos(4,2,3))
