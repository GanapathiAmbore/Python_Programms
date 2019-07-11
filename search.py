import re
x=input("enter a string")
y=re.match("ltd",x)
if y!=None:
    print("Match found!!")
else:
    print("Match not found!!")