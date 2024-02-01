#wamp to perform crud operation for covid patient in india
#crud create read update delete

data={}
while True:
	op=int(input("1 add new state,, 2 view state, 3 update state , 4 delete state and 5 exit "))
	if op == 1:
		sn=input("enter state name ")
		if data.get(sn) != None:
			print(sn, "already exits")
		else:
			co= int(input("enter count "))
			data[sn] = co
			print(sn, "added")
	elif op == 2:
		print(data)
	elif op == 3:
		sn=input("enter state name")
		if data.get(sn) == None:
			print(sn, "does not exit")
		else:
			co= int(input("enter count "))
			data[sn] = co
			print(sn, "updated")
	elif op == 4:
		sn=input("enter state name ")
		if data.get(sn) == None:
			print(sn, "does not exit")
		else:
			data.pop(sn)
			print(sn, "deleted")
	elif op == 5:
		break
	else:
		print("sorry i dont understand ")
			