def palindrome(x):
    rev=x[::-1]
    if x==rev:
        print("palindrome")
    else:
        print("Not a palindrome")
palindrome("OYo")
palindrome("dad")
palindrome("work")
palindrome("eye")
palindrome("111")