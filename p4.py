#wapp to read two set of name 
#find 



java =set()
res=input("do u want to enter the name y/n ")
while res =="y":
	n=input("inter the name in java ")
	java.add(n)
	res=input("do you want to enter more y/n ")


js=set()
res=input("do u want to enter the name y/n ")
while res =="y":
	n=input("inter the name js ")
	java.add(n)
	res=input("do you want to enter more y/n ")

print("name of all student =",java|js)
print("common student",java & js)
print("student in java =",java - js)
print("name in js but not in java=",js.difference(java))