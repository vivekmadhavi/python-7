#wapp to create state capital

sc = {
	"maharashtra"	:	"mumbai",
	"goa"	 	:	"panji",
	"gujrat"	:	"gandhinagar",
	"assam"		:	"guwahati",
	"rajasthan"	:	"jaipur",
	"delhi"		:	"delhi"

	}

print("welcome to state capital and press e for quick ")
while True:
	state=input("-->")
	if state =="e":
		print("thank you")
		break
	elif sc.get(state) == None:
		f= open("sorry.text", "a") # used for append operation
		f.write(state + "\n")
		f.close()
		print("sorry i dont understan")
	else:
		ans=sc.get(state)
		print(ans)