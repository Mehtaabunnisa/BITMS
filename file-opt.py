fileptr=open("example","r")
if fileptr:
     print("file is opened successfully")
     
fileptr=open("example","a")
fileptr.write("its example")
print(fileptr)
