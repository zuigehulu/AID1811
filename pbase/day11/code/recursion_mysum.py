def mysum(n):
    if n == 1:
        return 1
    return n + mysum(n-1)    

print(mysum(100))