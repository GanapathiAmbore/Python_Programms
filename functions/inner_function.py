def Foo(n):
    def multiplier(x):
        return x * n
    return multiplier
a = Foo(5)