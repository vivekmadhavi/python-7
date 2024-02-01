#wap to demo dict


#declare

d1={}
print(d1, type(d1))

d2 ={"idli":40 , "wada":50, "dosa":40}
print(d2, type(d2))

#add/update element

d1["idli"]=70
d1["poha"]=40
print(d1)
d1["poha"]=50
print(d1)

#remove

d1.pop("idli")
print(d1)
#di.pop("idli")
d1.clear()
print(d1)

#access
print(d2.get("idli"))
print(d2.get("tea"))

