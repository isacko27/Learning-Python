def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True


def contar_primos(num1):
    primos = []
    for num in range(2,num1):
        prime = is_prime(num)
        if prime:
            primos.append(num)
        else:
            pass
    return primos




def contar_primos_python(numero):

    primos = [2]
    iteracion = 3
    if numero < 2:
        return 0
    while iteracion <= numero:
        for n in range(3,iteracion,2):
            if iteracion % n == 0:
                iteracion += 2
                break
        else:
            primos.append(iteracion)
            iteracion +=2
    print(primos)
    return len(primos)

print(contar_primos(2000))
print(contar_primos_python(2000))