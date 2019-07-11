f=open("Tables.txt",'w')
x=int(input("Enter a number to print table!!"))
for j in range(1,x):
    for i in range(1,11):
        table=("j*i=j*i\n")
        f.write(table)