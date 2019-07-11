import re
x=input("enter a pincode to match")
y=re.fullmatch("[5]\d{5}",x)
if y!=None:
    print("Pincode is valid")
else:
    print("PIncode not valid")