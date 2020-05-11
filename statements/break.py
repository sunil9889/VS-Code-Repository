import random as r
i=1
while  i<=10:
   
    newRand=r.randint(4,20)
    print (newRand)
    if newRand==5:
        print("Break")
        break
    i+=1