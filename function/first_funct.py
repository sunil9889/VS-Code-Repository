def first_func():
    print("hello-world")
#execute function
#print(first_func) # to check where the function stored dynamically
first_func()

def nameCall(firstName,lastName):  #named function
    print("Hello " + firstName + " " +lastName ) # " " is for adding space 
nameCall(firstName="Sunil",lastName="kanaujiya")

def add_Num(arg1,arg2):
    add=arg1+arg2
    print(add)
add_Num(2,2)
