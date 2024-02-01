#wapp to read email addrss of student

data=set()

res=input("do u want to enter the email y/n ")
while res =="y":
	e=input("enter the email")
	data.add(e)
	res=input("do you want to enter more")
print(data)