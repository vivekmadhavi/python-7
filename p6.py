#wapp to implement simple chatbot

conv = {
	"h1"		:	"hello",
	"kamal batch" 	:	"yes",
	"java batch"	:	"jan to april",
	"java fees"	:	"rs 12000",
	"sir"		:	"kamal sir",
	"any discount"	:	"check other class"

	}

print("welcome to kamal classes chatbot and press q for quick ")
while True:
	qts=input("-->")
	if qts =="q":
		print("bye")
		break
	elif conv.get(qts) == None:
		print("sorry i dont understan")
	else:
		ans=conv.get(qts)
		print(ans)