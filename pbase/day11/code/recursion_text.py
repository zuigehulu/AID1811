def myyear(n):
    if n == 1:
        return 10
    return myyear(n-1)+2
print(myyear(3))
print(myyear(5))