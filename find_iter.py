import re
itr=re.finditer("[1-z]","a7b9c5k8z")
for m in itr:
    print(m.group())