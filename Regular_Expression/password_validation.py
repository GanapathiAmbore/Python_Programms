import re
x=input("enter a password to validate")
y=("[A-Za-z0-9@#$%^&+=]{8,}",x)
if y!=None:
    print("Valid password")
else:
    print("Invalid password")