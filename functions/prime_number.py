def prime(x):
    if x==2:
        return "prime"
    else:
        for i in range(2,x):
            if i%x==0:
                return "prime number"
            else:
                return "not prime"

print(prime(10))
print(prime(2))
print(prime(21))