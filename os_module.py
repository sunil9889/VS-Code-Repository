#import module
import os
#print(dir(os))
#print(help(os.getcwd))
#print(os.getcwd()) # get current working dir
# list directory all in which it is present uaing lisdir()
#print(os.listdir())
# change dir using os.chdir("/path")
os.chdir("D:/Python_Django/resources")
print(os.getcwd())
#make dir using os.makedirs("")  in current path 
#os.makedirs("newfolder") already ran so only one time to run
#isfile("Name of file/doc") check whether it is present in current dir or not
print(os.path.isfile("basics.pdf"))
print(os.path.isdir("newfolder"))
