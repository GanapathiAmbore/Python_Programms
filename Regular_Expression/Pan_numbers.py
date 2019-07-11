import re
x=input("Enter a PAN number:")
y=re.fullmatch("[A-Za-z]{5}\d{4}[A-Za-z]{1}",x)
if y!=None:
    print("Valid PAN Number")
else:
    print("Invalid PAN Number")
