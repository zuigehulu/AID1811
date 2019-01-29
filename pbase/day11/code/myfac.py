def myfac(n):
    if n == 0:
        return 1
    return n*myfac(n-1)

print(myfac(5))