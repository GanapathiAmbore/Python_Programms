import re
x=input("Enter a string to find")
y=re.findall('[a-z]',x)
print(y)