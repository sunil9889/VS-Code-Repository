import random
import sys
#variables
responses= ["It is certain","It is decidely so","Without a doubt",
"Yes definitly","Yes","signs point to yes","Outlook good",
"Ask again later","Maybe yes","Not confident"]
keep_asking="true"

#loop
while keep_asking:
    ques=input("Ask a question or press enter to exit")
    if ques=="":
        sys.exit()
    else:    
        print(responses[random.randint(0,9)])