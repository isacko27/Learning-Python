#Calcular comisiones del 13% con un programa que pregunte su nombre y cuanto ha vendido
#dar un resultado de la comision que le corresponde

nombre = input("Cual es tu nombre?: ")
venta = int(input("Cuanto vendiste?: "))

comision = round(venta * 13 / 100,2)
print(f"Hey broda {nombre} a vos te corresponde por tus ventas unos ${comision} de comision pana\n "
      f"Lo que en Total seria ${venta + comision} P ara ti bb, besitos en la nalga derecha")