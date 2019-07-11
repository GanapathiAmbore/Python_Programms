import re
x=input("enter a string to match")
y=re.fullmatch(x,"Ganapathi")
if y!=None:
    print("Match foud")
else:
    print("Match Not found")
