#f=open("file.txt","r")
#print(type(f))
#print(f.read())
#print(f.readline())
#print(f.read(5))
#for x in f:
 #   print(x.strip())
f=open( "file.txt","a") # w for write and replaces all data and 
#in append "a" we can append the data
f.write("\n extra line")
f.close()
#creating a file 
#f=open("file1.txt","x")
f=open("file1.txt","a")
f.write("hello")
f.close()