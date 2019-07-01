x=['abc', 'xyz', 'aba', '1221']
y=[]
for c in x:
    if len(c)>=2 and c[0]==c[-1]:
        y.append(c)
print(y)
