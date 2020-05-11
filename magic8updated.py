import random
import sys
#variables
ques= ["It is certain","It is decidely so","Without a doubt",
"Yes definitly","Yes","signs point to yes","Outlook good",
"Ask again later","Maybe yes","Not confident"]
keep_asking="true"
#i-=input(print("Enter y to play or n to stop"))
while keep_asking == "true":
        
        play_again=input("Let's Roll ? Y/N:")
        if play_again=="Y":
            print("Ok Rolling")           
            ask= input("enter you Question \n")   
            num=random.randint(0,9)
            print(ques[num]) 
        elif play_again=="N" :
            print("okay bye")
            keep_asking="false"
        else:
            print("Didn't understand Re-rolling") 


  