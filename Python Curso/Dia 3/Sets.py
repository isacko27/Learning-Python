mi_set = set([1,2,3,4,5,1,1,1,2,4,23,23])
print(type(mi_set))
print(mi_set)
print(2 in mi_set)
print(33 in mi_set)

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)
s1.add(4)
print(s1)

s1.remove(2)
print(s1)

s1.discard(6)
print(s1)

s1.discard(1)
print(s1)
s1.add((1,2,4,2,4,5,6,7,8))
print(s1)

aleatorio = s1.pop()#elimina aleatorio xd

print(aleatorio)