d={"a":"b"}
d1={1:2}
d2={2:2}
d3={}
for k in (d,d1,d2):
    d3.update(k)
print(d3)
