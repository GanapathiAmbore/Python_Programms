import re
x=input("Enter a PAN number:")
y=re.fullmatch("[A-Z]{5}[0-9][A-Z]$",x)
if y!=None:
    print("Valid PAN Number")
else:
    print("Invalid PAN Number")
