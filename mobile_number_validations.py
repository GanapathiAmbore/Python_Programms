import re
x=input("Enter a mobile number to match")
y=re.fullmatch("[6-9]\d{9}",x)
if y!=None:
    print("Number is matching")
else:
    print("Number is not matching")