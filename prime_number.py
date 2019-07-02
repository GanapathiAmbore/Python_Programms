def prime(x):
    if x==1:
        return "NOt a prime number"
    elif x==2:
        return "prime number"
    else:
        for i in range(2,x):
            if x%i==0:
                return "Not a prime number"
print(prime(21))
