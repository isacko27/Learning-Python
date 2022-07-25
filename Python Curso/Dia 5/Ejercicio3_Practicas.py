def cero_detect(*args):
    cero = 0
    for arg in args:
        if arg == 0:
            cero += 1
            if cero >= 2:
                return True
        else:
            pass
    return False

print(cero_detect(5,6,1,0,9,3,5))
print(cero_detect(5,6,1,0,0,9,3,5))