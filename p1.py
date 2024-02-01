#wapp to demo set

#declare

s1=set()
print(s1,type(s1))

s2=(10,20,40,30,20,30)
print(s2,type(s2))


# add element -->add() update()

s1.add(10)
s1.add(20)
s1.update([10,20,30,40,50])
print(s1)

#remove eleent --> remove(), discard(),clear()


s1.remove(10)
print(s1)
#s1.remove(40)

s1.discard(50)
print(s1)
s1.discard(50)
s1.clear()
print(s1)