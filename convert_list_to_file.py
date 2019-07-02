with open("numbers.txt",'w') as f:
    for i in range(101):
        f.write("%s\n"%i)
        print(i)

