x="python123"
l=[]
n=[]
for c in x:
    if c.isalpha():
        l.append(c)
    elif c.isdigit():
        n.append(c)
print(l,len(l))
print(n,len(l))