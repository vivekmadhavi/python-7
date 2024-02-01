#wapp to demo set operation

s1={10,20,30}
s2={40,10}

#union
print(s1|s2)
print(s1.union(s2))
print(s2.union(s1))

#intersection
print(s1&s2)
print(s1.intersection(s2))
print(s2.intersection(s1))

#different
print(s1 - s2)
print(s2 - s1)
print(s1.difference(s2))
print(s2.difference(s1))