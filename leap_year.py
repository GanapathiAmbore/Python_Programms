year=int(input("Enter a year"))
if year%4==0:
    print("leap year")
elif year%400==0:
    print("leap year")
elif year%100==0:
    print("not leap year")
else:
    print("Not leap year")
