dc={}
dc["one"]=(1,11)
dc["two"]=(2,22)
dc["three"]=(3,33)

file_pointer=open("temp.txt","w")

for x in dc:
	file_pointer.write(x+" "+str(dc[x])+"\n")
