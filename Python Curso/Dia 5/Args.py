def suma1(a,b):
    return a+b

def suma(*args):
    total = 0

    for arg in args:
        total += arg
    return total

print(suma1(5,6))
print(suma(5,6,4,2,2,32,42,4,2,3))