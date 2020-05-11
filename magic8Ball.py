import random as r
ans1="It is certain"
ans2="It is decidely so"
ans3="Without a doubt"
ans4="Yes , definitly"
ans5="Yes"
ans6="signs point to yes"
ans7="Outlook good"
ans8="Ask again later"
ans9="Maybe yes"
ans10="Not confident"
input("Ask me anything?")
i=r.randint(1,10)
if i==1:
    print(ans1)
elif i==2:
    print(ans2)
elif i==3:
    print(ans3)
elif i==4:
    print(ans4)
elif i==5:
    print(ans5)
elif i==6:
    print(ans6)
elif i==7:
    print(ans7)
elif i==8:
    print(ans8)
elif i==9:
    print(ans9)
else:
    print(ans10)

exit("")
