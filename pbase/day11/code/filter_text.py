def isprime(x):
    if x < 2:
        return False
    for ch in range(2,x):
        if x % ch == 0:
            return False
    return True
L = list(filter(isprime,range(100)))
print(L)
L = [x for x in filter(isprime,range(100))]
print(L)